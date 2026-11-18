
import org.apache.flink.api.common.state.ValueState;
import org.apache.flink.api.common.state.ValueStateDescriptor;
import org.apache.flink.api.common.typeinfo.Types;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.functions.KeyedProcessFunction;
import org.apache.flink.util.Collector;

import java.io.Serializable;
import java.time.Instant;

public class FraudDetectionJob {

    public static class Transaction implements Serializable {
        public String customerId;
        public double amount;
        public long timestamp;

        public Transaction() {}

        public Transaction(String customerId, double amount, long timestamp) {
            this.customerId = customerId;
            this.amount = amount;
            this.timestamp = timestamp;
        }
    }

    public static class FraudAlert implements Serializable {
        public String customerId;
        public double previousAmount;
        public double currentAmount;
        public long gapMs;

        public FraudAlert() {}

        public FraudAlert(String customerId, double previousAmount,
                          double currentAmount, long gapMs) {
            this.customerId = customerId;
            this.previousAmount = previousAmount;
            this.currentAmount = currentAmount;
            this.gapMs = gapMs;
        }

        @Override
        public String toString() {
            return "FRAUD ALERT: Customer=" + customerId
                    + ", Previous=₹" + previousAmount
                    + ", Current=₹" + currentAmount
                    + ", Gap=" + gapMs / 1000 + " seconds";
        }
    }

    public static class FraudDetector
            extends KeyedProcessFunction<String, Transaction, FraudAlert> {

        private transient ValueState<Transaction> previousTransaction;

        @Override
        public void open(
                org.apache.flink.configuration.Configuration parameters) {

            ValueStateDescriptor<Transaction> descriptor =
                    new ValueStateDescriptor<>(
                            "previous-large-transaction",
                            Types.POJO(Transaction.class));

            previousTransaction = getRuntimeContext().getState(descriptor);
        }

        @Override
        public void processElement(
                Transaction tx,
                Context ctx,
                Collector<FraudAlert> out) throws Exception {

            // Only consider transactions of ₹10,000 or more.
            if (tx.amount < 10000) {
                return;
            }

            Transaction previous = previousTransaction.value();

            if (previous != null) {
                long gap = tx.timestamp - previous.timestamp;

                if (gap >= 0 && gap <= 60000) {
                    out.collect(new FraudAlert(
                            tx.customerId,
                            previous.amount,
                            tx.amount,
                            gap));
                }
            }

            // Update the state for this customer.
            previousTransaction.update(tx);
        }
    }

    public static void main(String[] args) throws Exception {

        StreamExecutionEnvironment env =
                StreamExecutionEnvironment.getExecutionEnvironment();

        long base = Instant.parse("2026-10-19T10:00:00Z")
                .toEpochMilli();

        DataStream<Transaction> transactions = env.fromData(
                new Transaction("C101", 15000, base + 10000),
                new Transaction("C202", 5000, base + 20000),
                new Transaction("C101", 20000, base + 45000),
                new Transaction("C202", 12000, base + 50000),
                new Transaction("C101", 3000, base + 55000),
                new Transaction("C101", 18000, base + 90000),
                new Transaction("C202", 14000, base + 130000)
        );

        transactions
                .keyBy(tx -> tx.customerId)
                .process(new FraudDetector())
                .print();

        env.execute("Fraud Detection Job");
    }
}

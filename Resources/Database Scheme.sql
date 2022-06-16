-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "GPU" (
    "GPU_make" varchar(255)   NOT NULL,
    "GPU_name" varchar(255)   NOT NULL,
    "power_consumption" float   NOT NULL,
    "algorithm" varchar(255)   NOT NULL,
    "hastrate" float   NOT NULL,
    CONSTRAINT "pk_GPU" PRIMARY KEY (
        "GPU_name"
     )
);

CREATE TABLE "COST" (
    "GPU_make" varchar(255)   NOT NULL,
    "GPU_name" varchar(255)   NOT NULL,
    "GPU_cost" float   NOT NULL,
    CONSTRAINT "pk_COST" PRIMARY KEY (
        "GPU_name"
     )
);

CREATE TABLE "CRYPTO" (
    "tag" varchar(3)   NOT NULL,
    "algorithm" varchar(10)   NOT NULL,
    "block_time" float   NOT NULL,
    "block_reward" float   NOT NULL,
    "difficulty" float   NOT NULL,
    "network_hashrate" float   NOT NULL,
    "btc_revenue24" float   NOT NULL,
    "aud_revenue24" float   NOT NULL,
    CONSTRAINT "pk_CRYPTO" PRIMARY KEY (
        "tag"
     )
);

CREATE TABLE "MINING" (
    "GPU_name" varchar(255)   NOT NULL,
    "tag" varchar(3)   NOT NULL,
    "fixed_cost" float   NOT NULL,
    "operational_cost" float   NOT NULL,
    "revenue" float   NOT NULL,
    "profit" float   NOT NULL
);

ALTER TABLE "GPU" ADD CONSTRAINT "fk_GPU_GPU_name" FOREIGN KEY("GPU_name")
REFERENCES "MINING" ("GPU_name");

ALTER TABLE "GPU" ADD CONSTRAINT "fk_GPU_algorithm" FOREIGN KEY("algorithm")
REFERENCES "CRYPTO" ("algorithm");

ALTER TABLE "COST" ADD CONSTRAINT "fk_COST_GPU_make_GPU_name" FOREIGN KEY("GPU_make", "GPU_name")
REFERENCES "GPU" ("GPU_make", "GPU_name");

ALTER TABLE "CRYPTO" ADD CONSTRAINT "fk_CRYPTO_tag" FOREIGN KEY("tag")
REFERENCES "MINING" ("tag");


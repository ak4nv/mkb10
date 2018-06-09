CREATE TABLE IF NOT EXISTS "mkbo" ("id" INTEGER NOT NULL PRIMARY KEY, "parent_id" INTEGER, "name" TEXT NOT NULL, "name_lower" TEXT NOT NULL, "level" VARCHAR(1), "ict" VARCHAR(4), "code" VARCHAR(6), FOREIGN KEY ("parent_id") REFERENCES "mkbo" ("id"));
CREATE INDEX "mkbo_parent_id" ON "mkbo" ("parent_id");
CREATE INDEX "mkbo_name_lower" ON "mkbo" ("name_lower");
CREATE INDEX "mkbo_code" ON "mkbo" ("code");
CREATE TABLE IF NOT EXISTS "mkb10" ("id" INTEGER NOT NULL PRIMARY KEY, "rec_code" VARCHAR(8) NOT NULL, "code" VARCHAR(6), "name" TEXT NOT NULL, "name_lower" TEXT NOT NULL, "parent_id" INTEGER, "addl_code" INTEGER NOT NULL, "actual" INTEGER NOT NULL, "date" DATE, FOREIGN KEY ("parent_id") REFERENCES "mkb10" ("id"));
CREATE INDEX "mkb10_code" ON "mkb10" ("code");
CREATE INDEX "mkb10_name_lower" ON "mkb10" ("name_lower");
CREATE INDEX "mkb10_parent_id" ON "mkb10" ("parent_id");

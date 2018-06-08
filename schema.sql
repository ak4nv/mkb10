CREATE TABLE IF NOT EXISTS "mkb10" ("id" INTEGER NOT NULL PRIMARY KEY, "rec_code" VARCHAR(8) NOT NULL, "code" VARCHAR(6), "name" TEXT NOT NULL, "id_parent_id" INTEGER, "addl_code" INTEGER NOT NULL, "actual" INTEGER NOT NULL, "date" DATE, FOREIGN KEY ("id_parent_id") REFERENCES "mkb10" ("id"));
CREATE INDEX "mkb10_code" ON "mkb10" ("code");
CREATE INDEX "mkb10_name" ON "mkb10" ("name");
CREATE INDEX "mkb10_id_parent_id" ON "mkb10" ("id_parent_id");
CREATE TABLE IF NOT EXISTS "mkbo" ("id" INTEGER NOT NULL PRIMARY KEY, "id_parent_id" INTEGER, "name" TEXT NOT NULL, "level" VARCHAR(1), "ict" VARCHAR(4), "code" VARCHAR(6), FOREIGN KEY ("id_parent_id") REFERENCES "mkbo" ("id"));
CREATE INDEX "mkbo_id_parent_id" ON "mkbo" ("id_parent_id");
CREATE INDEX "mkbo_name" ON "mkbo" ("name");
CREATE INDEX "mkbo_code" ON "mkbo" ("code");

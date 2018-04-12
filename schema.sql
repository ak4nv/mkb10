CREATE TABLE IF NOT EXISTS "mkb10" ("id" INTEGER NOT NULL PRIMARY KEY, "rec_code" VARCHAR(8) NOT NULL, "code" VARCHAR(6), "name" TEXT NOT NULL, "id_parent_id" INTEGER, "addl_code" INTEGER NOT NULL, "actual" INTEGER NOT NULL, "date" DATE, FOREIGN KEY ("id_parent_id") REFERENCES "mkb10" ("id"));
CREATE INDEX "mkb10_code" ON "mkb10" ("code");
CREATE INDEX "mkb10_name" ON "mkb10" ("name");
CREATE INDEX "mkb10_id_parent_id" ON "mkb10" ("id_parent_id");
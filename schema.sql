CREATE TABLE IF NOT EXISTS "mkb10" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "rec_code" VARCHAR(8) NOT NULL,
  "code" VARCHAR(6),
  "name" TEXT NOT NULL,
  "parent_id" INTEGER,
  "addl_code" INTEGER NOT NULL,
  "actual" INTEGER NOT NULL,
  "date" DATE,
  FOREIGN KEY ("parent_id") REFERENCES "mkb10" ("id")
);
CREATE INDEX "mkb10_code" ON "mkb10" ("code");
CREATE INDEX "mkb10_name" ON "mkb10" ("name");
CREATE INDEX "mkb10_parent_id" ON "mkb10" ("parent_id");

CREATE TABLE IF NOT EXISTS "mkbo" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "parent_id" INTEGER,
  "code" VARCHAR(6),
  "name" TEXT NOT NULL,
  "synonym" VARCHAR(4),
  FOREIGN KEY ("parent_id") REFERENCES "mkbo" ("id")
);
CREATE INDEX "mkbo_parent_id" ON "mkbo" ("parent_id");
CREATE INDEX "mkbo_name" ON "mkbo" ("name");
CREATE INDEX "mkbo_code" ON "mkbo" ("code");

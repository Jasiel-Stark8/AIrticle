CREATE TABLE "Articles Table"(
    "article_id" SERIAL NOT NULL,
    "user_id" INTEGER NULL,
    "title" TEXT NULL,
    "content" TEXT NULL,
    "last_saved" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "export_format" TEXT NULL
);
ALTER TABLE
    "Articles Table" ADD PRIMARY KEY("article_id");
COMMENT
ON COLUMN
    "Articles Table"."article_id" IS 'Unique identifier for articles';
COMMENT
ON COLUMN
    "Articles Table"."user_id" IS 'Reference to Users table';
COMMENT
ON COLUMN
    "Articles Table"."title" IS 'Title of the article';
COMMENT
ON COLUMN
    "Articles Table"."content" IS 'Content of the article';
COMMENT
ON COLUMN
    "Articles Table"."last_saved" IS 'Last saved timestamp';
COMMENT
ON COLUMN
    "Articles Table"."export_format" IS 'Export format (DOC, DOCX, PDF, TXT)';
CREATE TABLE "Users Table"(
    "user_id" SERIAL NOT NULL,
    "email" TEXT NULL,
    "password_hash" TEXT NULL
);
ALTER TABLE
    "Users Table" ADD PRIMARY KEY("user_id");
ALTER TABLE
    "Users Table" ADD CONSTRAINT "users table_email_unique" UNIQUE("email");
COMMENT
ON COLUMN
    "Users Table"."user_id" IS 'Unique identifier for users';
COMMENT
ON COLUMN
    "Users Table"."email" IS 'User''s email address';
COMMENT
ON COLUMN
    "Users Table"."password_hash" IS 'Hashed password';
CREATE TABLE "AutoSave Table"(
    "autosave_id" SERIAL NOT NULL,
    "article_id" INTEGER NULL,
    "content" TEXT NULL,
    "timestamp" TIMESTAMP(0) WITHOUT TIME ZONE NULL
);
ALTER TABLE
    "AutoSave Table" ADD PRIMARY KEY("autosave_id");
COMMENT
ON COLUMN
    "AutoSave Table"."autosave_id" IS 'Unique identifier for autosave';
COMMENT
ON COLUMN
    "AutoSave Table"."article_id" IS 'Reference to Articles table';
COMMENT
ON COLUMN
    "AutoSave Table"."content" IS 'Autosaved content';
COMMENT
ON COLUMN
    "AutoSave Table"."timestamp" IS 'Autosave timestamp';
ALTER TABLE
    "AutoSave Table" ADD CONSTRAINT "autosave table_article_id_foreign" FOREIGN KEY("article_id") REFERENCES "Articles Table"("article_id");
ALTER TABLE
    "Articles Table" ADD CONSTRAINT "articles table_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "Users Table"("user_id");
create table Users (
    UserName text primary key,
    PassWord bytea not null,
    pass_nonce bytea not null,
    pass_tag bytea not null,
    UpdateDate timestamp not null
);

create table Articles (
    ArticleId serial primary key,
    Title text not null,
    Content text not null,
    UpdateDate timestamp not null
);
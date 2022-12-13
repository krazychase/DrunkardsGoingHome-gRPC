CREATE TABLE Users (
    UserID          INT PRIMARY KEY AUTOINCREMENT ,
    Username        varchar(255),
    Password        varchar(255),
    HomeLocation    varchar(255)
);
CREATE TABLE Rides (
    RideID          INT PRIMARY KEY AUTOINCREMENT ,
    Rider           INT,
    Driver          INT,
    Destination     varchar(255),
    Location        varchar(255),
    Time            DATETIME,
    Status          varchar(255)
);
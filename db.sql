use history;

drop table if exists calls;

create table calls (
    id int not null AUTO_INCREMENT, -- ТУТ
    start_time datetime,
    duration int,
    from_phone varchar(15),
    connected_to_phone int,
    disposition varchar(50),
    global_interaction_id int,      -- И тут я схалявил, уж извините :)
    primary key (id)
);

insert into calls(start_time, duration, from_phone, connected_to_phone, disposition, global_interaction_id)
    values ('2018-02-12 11:05:58', 10, 19169, 2061, 'CALLEEE_TERMINATED', 1236544);

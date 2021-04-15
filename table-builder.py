import random
from datetime import datetime, date, time

#insert into calls(start_time, duration, from_phone, connected_to_phone, disposition, global_interaction_id)
#    values ('2018-02-12 11:05:58', 10, 19169, 2061, 'CALLEEE_TERMINATED', 1236544);

x = "asdasd"
for i in range(0, 100):
    print(
    f"""insert into calls(start_time, duration, from_phone, connected_to_phone, disposition, global_interaction_id)
    values ('{
        datetime(2021, 4, random.randrange(11,16), 16, 29, 43)}', {
            random.randrange(1,10000)}, 19169, 2061, '{
                random.choice(['CALLEEE_TERMINATED', "ABANDONED", "NO_ANSWER","SYSTEM_DISCONNECTED" ])}', 1236544);"""
    )
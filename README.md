# locust_performance_test

Example calls used in our tests:

Master node:

```
locust --host=https://meeting.test.up2university.eu --master
```

Slave node:

```
locust --host=https://meeting.test.up2university.eu :500 --slave--master-host=”master node host”
```

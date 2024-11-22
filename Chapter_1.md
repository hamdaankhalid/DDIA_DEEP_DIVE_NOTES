# Reliability, Scalability, Maintainability

- Shift in industry from CPU intensive to Data intensive problems. Talk about examples, and how compute is becoming important again with rise of AI
- Shift in application need for specifc tools as opposed to one data tool for everything. Now we have blurred lines between storage systems and message queues etc.
- Today even application level engineers are stiching together tools to create composite data systems that makes them not only application deves, but also data system designers. Data systems need to be built with pillars in mind, discussed in this chapter.


## Defns
- Reliability: System should continue to work correctly even in th face of adversity (hware/software/human faults)
- Scalability: As system grows (data volume, traffic, complexity) there should be reasonable ways of dealing with said growth.
- Maintainability: Over time, many different people will work on the system (engineering and operations, both maintaining current behavior and adapting the system to new use cases), and they should all be able to work on it productively. Segue to discuss how this is the least solved problem out of the above 3 imo


### Reliability/Resiliency

**What does it mean to work correctly?**

For software, typical expectations include:
- The application performs the function that the user expected.
- It can tolerate the user making mistakes or using the software in unexpected ways.
- Its performance is good enough for the required use case, under the expected load and data volume.
- The system prevents any unauthorized access and abuse.
If all those things together mean “working correctly,” then we can understand reliability as meaning, roughly, “continuing to work correctly, even when things go wrong.”

- Note that a fault is not the same as a failure. A fault is usually defined as one component of the system deviating from its spec, whereas a failure is when the system as a whole stops providing the required service to the user. It is impossible to reduce the probability of a fault to zero; therefore it is usually best to design fault-tolerance mechanisms that prevent faults from causing failures.

- Chaos Monkey, and alternatives to inject faults in system for resiliency testing.

#### Hardware Faults
- Hard disks crash, RAM becomes faulty, the power grid has a blackout, someone unplugs the wrong network cable
- More servers, more problems: Hard disks are reported as having a mean time to failure (MTTF) of about 10 to 50 years [5, 6]. Thus, on a storage cluster with 10,000 disks, we should expect on average one disk to die per day. (TODO add mathematical explanation)
- Redundancy (example raid, hotswappable CPUS, Data centers having backup power sources). When one component dies, the redundant component can take its place while the broken component is replaced.
- However, as data volumes and applications’ computing demands have increased, more applications have begun using larger numbers of machines, which proportionally increases the rate of hardware faults.
- Industry moving toward systems that can tolerate the loss of entire machines, by using software fault-tolerance techniques in preference or in addition to hardware redundancy. High Availability


#### Software Faults, Human faults
- Very different from Hardware faults, can cascade, corrupt systems, no quick solutions except, careful thinking, testing, process isolation, allowing things to crash in violation of invariants (this is why you dont catch everything), measuring, monitoring, and analyzing systems in production. SET alerts around invariantas!!! because we write bugs, and need a watch dog. (Define invariants), Microsoft SDP standards


### Scalability
- it is meaningless to say “X is scalable” or “Y doesn’t scale.” Rather, discussing scalability means considering questions like “If the system grows in a particular way, what are our options for coping with the growth?” and “How can we add computing resources to handle the additional load?”

- Scalability isn’t an inherent system feature; it depends on the system’s ability to handle specific types of growth.
- Key questions to consider:
    * How can we manage growth in data volume, traffic, or complexity?
    * Can we add resources to handle additional load effectively?

#### Defining Load
- Load parameters depend on the system’s architecture, such as:
    * Requests per second (e.g., web servers).
    * Read/write ratios (e.g., databases).
    * Concurrent users (e.g., chat applications).
- Some systems exhibit asymmetrical read/write paths, such as:
    * Twitter, where read and write loads differ significantly due to fanout patterns.
    * Indexing applications, where write latency may be less critical than read performance.

#### Performance Metrics
**Latency vs. Response Time**
- Latency: Time required to complete a task.
- Response time: Total delay experienced by a client, including network and queuing delays.
- Throughput: Measures the rate at which the system processes tasks.

#### Percentile Response Times
- Quick explain using example of 100ms at 50p, 90p, 99p
Percentiles provide a better description of latency, particularly in performance analysis, because they give a clearer picture of the range and distribution of response times rather than just summarizing the data as an average or percentage. Here’s why they’re particularly useful for latency:
Handling Outliers: Unlike averages, percentiles can illustrate how many requests fall into slower response times, showing tail latency. For instance, a 95th or 99th percentile latency tells you the response time that 95% or 99% of requests achieve, highlighting the slowest end of the experience without skewing the entire metric as an average would.
User Experience: Percentiles align more closely with real user experience by indicating the response time most users can expect. For instance, a 95th percentile latency of 200ms means that 95% of requests finish in under 200ms, while the 5% slowest may be higher. This helps capture those edge cases that impact users but are lost in an average.
Performance Benchmarks: Percentiles allow you to set more meaningful service level objectives (SLOs). For example, aiming for a 99th percentile latency target is often more practical for performance goals than trying to minimize average latency, which doesn’t account for worst-case scenarios.
Granular Insights: By using different percentiles (e.g., 50th, 90th, 99th), you get a more detailed view of the latency profile, as opposed to an average that gives a single value. This granularity helps in understanding both the typical and the worst-case latencies.

Example: High-value customers with large datasets may experience slower response times.
Service Level Objectives (SLOs) and Service Level Agreements (SLAs)
Set performance expectations for latency, throughput, etc.

#### Load Testing
Ensures the system can handle anticipated conditions and meet SLAs.

#### Coping with Load
- Vertical Scaling (Scale-Up): Adding more power to individual machines (e.g., more CPU/RAM).
- Horizontal Scaling (Scale-Out): Adding more machines to distribute the load. Often employs shared-nothing architectures to minimize dependencies between nodes, enabling efficient scaling.

Scalability considerations play a critical role in designing robust, adaptable systems that can meet user demands under growing loads and evolving conditions.

### Maintainability
A maintainable system can be operated, modified, and evolved efficiently by various people over time. As systems are managed and adapted by both engineers and operations teams, maintainability hinges on three essential attributes: operability, simplicity, and evolvability.
- Operability involves ensuring that the system runs smoothly and can be easily monitored and controlled. Good operability reduces the amount of manual intervention required and ensures that the system can handle both expected and unexpected events.
- Simplicity makes the system easier to understand, which aids in troubleshooting and lowers the chances of introducing bugs during updates. Simple systems reduce cognitive load on developers, who can focus on meaningful work rather than navigating complex interactions.
- Evolvability is crucial for long-term success, enabling the system to adapt to new business needs, technologies, and user expectations. Systems designed with modular components or APIs, for instance, are easier to update and extend.

Maintainability considerations are often overlooked during initial system design but become critical as systems grow and change over time.


## Discuss:

- Google's IRS tail latency case study: https://cacm.acm.org/research/the-tail-at-scale/

### Talking points
- Variability of response times can produce higher tail latency. Look at section on variability.
- Variability probability increases with more nodes in cluster.
- Variability in the latency distribution of individual components is magnified at the service level; for example, consider a system where each server typically responds in 10ms but with a 99th-percentile latency of one second. If a user request is handled on just one such server, one user request in 100 will be slow (one second). If a user request must collect responses from 100 such servers in parallel, then 63% of user requests will take more than one second. Even for services with only one in 10,000 requests experiencing more than one-second latencies at the single-server level, a service with 2,000 such servers will see almost one in five user requests taking more than one second.

P(one request in a single server taking longer than 1 seconds) = 0.1
P(one reqest in parallel to a cluster of 100 server taking longer than 1 sec) = 1 - P(no sever out of the 100 takes longer than 1 sec) = 1 - (0.9^100)

#### Reducing Variability: (TODO add more explanation)
- Differentiating service classes and higher level queueing.
- Reducing head of line blocking
- Managing background activites and synchronized disruption

#### Google's tail tolerant techniques:

**Within Request Short-Term Adaptations**
- hedged requests, send secondary request to another replica if first is past a threshold
- Tied requests: more aggressive since hedged may not offer enough optimization because we are still waiting for 95 percentile crossing. Permitting more aggressive use of hedged requests with moderate resource consumption requires faster cancellation of requests. Issue multiple reqs and let the servers talk to each other so that the first caller cancels others
- An alternative to the tied-request and hedged-request schemes is to probe remote queues first, then submit the request to the least-loaded server.10 It can be beneficial but is less effective than submitting work to two queues simultaneously for three main reasons: load levels can change between probe and request time; request service times can be difficult to estimate due to underlying system and hardware variability; and clients can create temporary hot spots by all clients picking the same (least-loaded) server at the same time. The Distributed Shortest-Positioning Time First system9 uses another variation in which the request is sent to one server and forwarded to replicas only if the initial server does not have it in its cache and uses cross-server cancellations.
-  The class of techniques described here is effective only when the phenomena that causes variability does not tend to simultaneously affect multiple request replicas. We expect such uncorrelated phenomena are rather common in large-scale systems.

**Cross-Request Long-Term Adaptations**
Although many systems try to partition data in such a way that the partitions have equal cost, a static assignment of a single partition to each machine is rarely sufficient in practice for two reasons: First, the performance of the underlying machines is neither uniform nor constant over time, for reasons (such as thermal throttling and shared workload interference). And second, outliers in the assignment of items to partitions can cause data-induced load imbalance (such as when a particular item becomes popular and the load for its partition increases).
- Microrepetitions
- Selective replication
- Latency-induced probation, IDK how realistically helps let a server recover, since we need to reduce its load very often for letting it recover, and shadow requests are contradictory


**Google specific Case in IRS**
- A simple way to curb latency variability is to issue the same request to multiple replicas and use the results from whichever replica responds first.
- Sometimes they dont even need all requests, they can choose good enough over perfect when the cost is response time. (users notice response time closely).

#### Tail latency in Write path
- Everything till now handled tail latency tolerance in read paths.
- Tolerating latency variability for operations that mutate state is somewhat easier for a number of reasons: 
    * the scale of latency-critical modifications in these services is generally small. Nature of most Data intensive systems today.
    * updates can often be performed off the critical path, after responding to the user (instagram, FB)
    * many services can be structured to tolerate inconsistent update models for (inherently more latency-tolerant) mutations (not strong consistent)
    * for those services that require consistent updates, the most commonly used techniques are quorum-based algorithms (such as Lamport’s Paxos8); since these algorithms must commit to only three to five replicas, they are inherently tail-tolerant.

### Should We code something discussed above? What are the suggestions? Hedged reqs?
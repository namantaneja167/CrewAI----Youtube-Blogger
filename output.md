**Optimizing Storage Costs with Amazon S3 Glacier Instant Retrieval: Canva's Journey**

**Introduction**
Canva, the popular online design tool, has seen tremendous growth since its launch in 2013. With over 100 million active monthly users and more than 15 billion designs created, Canva's data storage needs have skyrocketed, accumulating over 230 Petabytes of data across Amazon S3 storage. Managing these vast amounts of data efficiently became crucial for Canva.

**Introduction to Amazon S3 and Storage Classes**
Amazon S3 is a cloud storage service that allows users to store data as objects in buckets, each with a unique URL for easy access. S3 offers various storage classes to balance cost and access needs:
- **S3 Standard:** Best for frequently accessed data.
- **S3 Standard-IA:** Cheaper for less frequently accessed data.
- **S3 Glacier Flexible Retrieval:** Low-cost archival storage with longer retrieval times.
- **S3 Glacier Instant Retrieval:** Introduced in November 2021, offers lower storage costs while providing millisecond retrieval times.

**Cost Analysis and Migration Strategy**
Canva utilized S3 Storage Class Analysis to understand their data usage. They discovered that user-generated content was frequently accessed within the first 15 days but dropped significantly afterward. About 90% of their data was stored in S3 Standard-IA, accounting for only 30-40% of all data accesses. The analysis revealed that much of Canva's data was suitable for S3 Glacier Instant Retrieval.

Potential savings for 207 PB (90% of 230 PB) were significant:
- **S3 Standard-IA cost:** $0.0125 per GB per month = $2,587,500
- **S3 Glacier Instant Retrieval cost:** $0.0036 per GB per month = $745,200
- **Savings:** $1,842,300 per month or $22,107,600 per year

**Key Considerations:**
- **Minimum Billable Object Size:** S3 Glacier Instant Retrieval has a minimum billable object size of 128KB.
- **Transition Costs:** One-time fee of $0.02 per 1000 objects could cost over $6 million for 300 billion objects.

**Implementation Results**
Canva's migration strategy was straightforward. They applied lifecycle policies to S3 buckets, automatically migrating objects to S3 Glacier Instant Retrieval based on predefined rules. This process was highly efficient, with Canva successfully migrating nearly 80 billion objects in two days. After the migration, 130 PB out of 230 PB of data now reside in S3 Glacier Instant Retrieval.

**Results:**
- **Cost Savings:** Roughly $300,000 per month or $3.6 million per year.
- **Break-even Point:** Prioritized objects larger than 400KB to ensure a positive return on investment within six months.

**Key Points:**
- Canva's massive data storage needs led to exploring cost-efficient solutions.
- S3 Glacier Instant Retrieval offers significant savings for infrequently accessed data requiring fast retrieval.
- Meticulous analysis and strategic implementation ensured cost-effectiveness and quick ROI.
- Resulted in substantial monthly and annual savings.s
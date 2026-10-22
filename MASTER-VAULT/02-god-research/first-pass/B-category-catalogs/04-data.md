# 04 — Data (Relational/NoSQL/Graph/Vector/Search · ORMs · Migrations · Caching · Storage)

> Part 3 · B-category catalog · Core-Tech researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved

## Index (24 resources)

Relational: PostgreSQL · MySQL · SQLite (+libSQL/Turso) · CockroachDB
NoSQL/KV/Docs: MongoDB · Redis/Valkey · Cassandra/Scylla (columnar)
Graph: Neo4j
Search: Elasticsearch · Meilisearch · Typesense
Vector: Pinecone (managed) · Weaviate · Qdrant · pgvector
ORMs/Query: Prisma · Drizzle · SQLAlchemy (+Alembic) · Kysely
Migrations/ops: Flyway · Atlas (declarative)
Caching/CDN edge: Cloudflare Workers KV / Upstash (serverless Redis)
Storage/Media store: S3 + MinIO · Cloudinary (also in 05-media)

---

### 01 — PostgreSQL (17/18 + 19 beta)
- **Canonical identity:** `db:postgresql` — PostgreSQL Global Development Group
- **Category:** Data → Relational (ORDBMS)
- **Type:** OSS RDBMS
- **Official URL:** https://www.postgresql.org/ (docs: https://www.postgresql.org/docs/)
- **Description:** Most-advanced OSS relational; JSONB, arrays, GIN/GiST, full-text, PostGIS/pgvector extensions; 35+ years; 19 Beta 4 (2026-09-24), 18.6/17.11 patch (2026-08-13).
- **Contents inspected:** WebFetch postgresql.org homepage 2026-10-09 (news: 19 Beta 4, JDBC CVE note, pgx-bm25/pg_ivm items; event list Oct-2026; release table verified).
- **Capabilities:** ACID, MVCC, CTEs/windows, logical replication, partitioning, RLS, `pgvector`/`pg_trgm`/`PostGIS`.
- **Usage domain:** Default OLTP + analytics + vector/search hybrid.
- **Integration:** native (psql/libpq; drivers: `pg`, `postgres.js`, Prisma/Drizzle/SQLAlchemy; Prisma Postgres managed)
- **Compatibility:** v14 EOL 2026-11-12 → run 15+; 17/18 current.
- **Deps:** None (extensions optional).
- **Availability:** postgresql.org/download; Docker `postgres:`; managed (Neon/Supabase/RDS/Prisma Postgres).
- **Maintenance:** Active (yearly majors; 5-year minors).
- **License:** PostgreSQL License (permissive, BSD-like).
- **Security/limits:** `pg_hba`/SCRAM, RLS policies, `SECURITY DEFINER` audits; connection pooling (PgBouncer/Supavisor) for serverless.
- **Related:** CockroachDB, MySQL, Prisma, Drizzle, pgvector.
- **Sources:** WebFetch postgresql.org (this session).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — MySQL (8.x + HeatWave) / MariaDB fork note
- **Canonical identity:** `db:mysql` (Oracle) + `db:mariadb` fork
- **Category:** Data → Relational
- **Type:** OSS (GPL) + commercial
- **Official URLs:** https://www.mysql.com/ (docs: https://dev.mysql.com/doc/) · https://mariadb.org/
- **Description:** Ubiquitous LAMP/WordPress/legacy SaaS; InnoDB, replicas, JSON; MariaDB is community fork (feature-diverged).
- **Contents inspected:** dev.mysql.com 8.0/8.4 reference TOC (search-verified).
- **Capabilities:** GTID replication, Group Replication/InnoDB Cluster.
- **Usage domain:** CMS, commerce, cPanel fleets.
- **Integration:** native (mysql2, Prisma/Drizzle/TypeORM; PlanetScale Vitess-compatible serverless)
- **Compatibility:** 8.0/8.4 LTS; MariaDB not drop-in for newest features.
- **Deps:** None.
- **Availability:** dev.mysql.com downloads; Docker; RDS/Cloud SQL/PlanetScale.
- **Maintenance:** Active (Oracle + MariaDB Foundation).
- **License:** GPL-2.0 (community) / commercial.
- **Security/limits:** `caching_sha2_password`, blind `SELECT ... INTO` hygiene; GPL implications for embedded distribution.
- **Related:** Postgres (migration target), TiDB, Vitess.
- **Sources:** dev.mysql.com; mariadb.org.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 03 — SQLite (+ libSQL / Turso)
- **Canonical identity:** `db:sqlite` (public domain) + `tool:libsql`/`saas:turso`
- **Category:** Data → Embedded relational
- **Type:** OSS library + managed edge replicas
- **Official URLs:** https://www.sqlite.org/ · https://turso.tech/ (docs: https://docs.turso.tech/)
- **Description:** Zero-config file DB; WAL, FTS5, JSON1, `sqlite-vec`; libSQL fork adds replication; Turso edge-hosts it; Drizzle/Prisma support.
- **Contents inspected:** sqlite.org docs (lang/FTS); Turso quickstarts (search-verified).
- **Capabilities:** Single-writer + read replicas; `rqlite/LiteFS` for HA; Cloudflare D1 (SQLite-at-edge cousin).
- **Usage domain:** Mobile, edge, CLI tools, small SaaS, tests.
- **Integration:** official (`better-sqlite3`, `@libsql/client`, Drizzle `drizzle-orm/libsql`, Prisma `sqlite` provider)
- **Compatibility:** All OSes; WASM builds (`wa-sqlite`, PGLite for Postgres-in-WASM).
- **Deps:** None.
- **Availability:** Public domain amalgamation; npm clients.
- **Maintenance:** Active (3.4x/3.5x 2025-2026).
- **License:** Public domain (SQLite); MIT/Apache (libSQL/Turso clients).
- **Security/limits:** File perms + `PRAGMA journal_mode=WAL`; Internet-exposed SQLite files must never be web-served.
- **Related:** Postgres (scale-up), DuckDB (OLAP cousin), D1.
- **Sources:** sqlite.org; docs.turso.tech.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 04 — CockroachDB (Postgres-compatible distributed)
- **Canonical identity:** `db:cockroachdb` — Cockroach Labs
- **Category:** Data → Distributed SQL
- **Type:** Source-available/commercial (BSL) + Serverless
- **Official URL:** https://www.cockroachlabs.com/ (docs: https://www.cockroachlabs.com/docs/)
- **Description:** Geo-distributed Postgres-wire SQL; survival goals, online schema; good for multi-region SaaS.
- **Contents inspected:** CockroachDB docs (deploy, SQL parity notes).
- **Capabilities:** Serializable, follower reads, changefeeds (CDC).
- **Usage domain:** Fintech/global SaaS needing HA.
- **Integration:** native (PG drivers + Prisma/Drizzle via PG dialect)
- **Compatibility:** PG-wire mostly; some PG features differ (check parity).
- **Deps:** None.
- **Availability:** Self-host + Dedicated/Serverless.
- **Maintenance:** Active (v23/24 2024-2026).
- **License:** BSL 1.1 (core; converts to Apache after years) — review for self-host.
- **Security/limits:** Enterprise encryption/RBAC in paid tiers; cert-based inter-node auth.
- **Related:** YugabyteDB, Spanner, Postgres.
- **Sources:** cockroachlabs docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 05 — MongoDB (8.x, Document)
- **Canonical identity:** `db:mongodb` — MongoDB Inc.
- **Category:** Data → Document NoSQL
- **Type:** OSS (SSPL) + Atlas managed
- **Official URL:** https://www.mongodb.com/ (docs: https://www.mongodb.com/docs/)
- **Description:** BSON collections, aggregation pipeline, Atlas Search/Vector Search, change streams, time series.
- **Contents inspected:** MongoDB docs hub (CRUD/aggregation/Atlas).
- **Capabilities:** Flexible schema + schema validation, transactions (multi-doc), sharding.
- **Usage domain:** Catalogs, CMS, event stores, prototyping.
- **Integration:** official (`mongoose`, `mongodb` driver, Prisma `mongodb` provider)
- **Compatibility:** 7.0/8.0; Atlas evergreen.
- **Deps:** None.
- **Availability:** Community + Atlas free tier.
- **Maintenance:** Active.
- **License:** SSPL (server; copyleft-network) — Atlas or Enterprise for commercial hosting nuance.
- **Security/limits:** Auth + TLS +Queryable Encryption for PII; injection via `$where`/unvalidated operators.
- **Related:** FerretDB (PG-backed alt), DocumentDB, Couchbase.
- **Sources:** mongodb.com/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 06 — Redis (7.x) + Valkey fork note
- **Canonical identity:** `db:redis` (Redis Ltd) + `db:valkey` (Linux Foundation fork)
- **Category:** Data → In-memory KV/cache/broker
- **Type:** Source-available (RSAL/SSPL+AGPL mix post-2024) vs OSS fork
- **Official URLs:** https://redis.io/ · https://valkey.io/ (serverless: https://upstash.com/)
- **Description:** Strings/hashes/streams/pubsub, Lua, modules (Search/JSON); Valkey is MIT-community continuation; Upstash serverless Redis for edge.
- **Contents inspected:** redis.io + valkey.io docs; BullMQ compat notes.
- **Capabilities:** TTL, transactions, streams (queue), Cluster/Sentinel.
- **Usage domain:** Cache, sessions, rate-limit, queues (BullMQ), realtime adapters.
- **Integration:** official (`ioredis`, `node-redis`; `@socket.io/redis-adapter`)
- **Compatibility:** RESP2/3; Redis 6.2+ streams baseline.
- **Deps:** None.
- **Availability:** Docker; managed (Upstash/ElastiCache/Memorystore).
- **Maintenance:** Active (both lines; choose per license policy).
- **License:** Redis RSALv2/SSPLv1+AGPLv3 (review!) / Valkey BSD-3-Clause.
- **Security/limits:** AUTH+TLS, `protected-mode`, keyspace PII TTLs; persistence (AOF/RDB) sizing.
- **Related:** Memcached, Dragonfly, Garnet.
- **Sources:** redis.io; valkey.io.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 07 — Apache Cassandra / ScyllaDB (wide-column)
- **Canonical identities:** `db:cassandra` (Apache) · `db:scylladb` (C++-compatible)
- **Category:** Data → Wide-column NoSQL
- **Type:** OSS
- **Official URLs:** https://cassandra.apache.org/ · https://www.scylladb.com/ (docs hubs)
- **Description:** Linear-scale writes, tunable consistency, CQL; Scylla drop-in with lower tail latency.
- **Contents inspected:** Cassandra 4.1/5.0 + Scylla docs TOCs.
- **Capabilities:** Multi-DC replication, lightweight transactions (Paxos), CDC.
- **Usage domain:** IoT/telemetry, messaging history, high-write.
- **Integration:** official drivers (DataStax Node/Python/Go)
- **Compatibility:** CQL; Scylla mostly wire-compatible.
- **Deps:** JVM (Cassandra) / Seastar (Scylla).
- **Availability:** Docker; managed (Astra DB, Scylla Cloud).
- **Maintenance:** Active.
- **License:** Apache-2.0 (Cassandra); Apache/SSPL mix checks per Scylla component (verify).
- **Security/limits:** Internode/client TLS + RBAC (DSE features vary OSS vs Enterprise).
- **Related:** Bigtable, HBase, DynamoDB.
- **Sources:** Official docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 08 — Neo4j (Graph)
- **Canonical identity:** `db:neo4j` — Neo4j Inc.
- **Category:** Data → Property graph
- **Type:** Source-available/commercial (GPL Community + Enterprise)
- **Official URL:** https://neo4j.com/ (docs: https://neo4j.com/docs/)
- **Description:** Cypher/GQL, Graph Data Science lib, Aura managed; fraud/recs/knowledge-graph leader.
- **Contents inspected:** Neo4j docs (Cypher manual, Aura).
- **Capabilities:** Traversals, pathfinding, embeddings + vector index (hybrid graph+RAG).
- **Usage domain:** Fraud, IAM graphs, recommendations, KG-RAG.
- **Integration:** official drivers (`neo4j-driver`, `neomodel`, LangChain graph QA)
- **Compatibility:** 5.x; Aura evergreen.
- **Deps:** JVM.
- **Availability:** Desktop/Community + Aura free tier.
- **Maintenance:** Active.
- **License:** GPL-3.0 (Community) / commercial (Enterprise/Aura).
- **Security/limits:** Role-based + query allowlist; Cypher injection via string concat — parameterize.
- **Related:** Memgraph, Neptune, TigerGraph, Kuzu (embedded alt).
- **Sources:** neo4j.com/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 09 — Elasticsearch (8.x) — search/analytics exemplar
- **Canonical identity:** `tool:elasticsearch` — Elastic
- **Category:** Data → Search + analytics
- **Type:** Source-available (SSPL/Elastic License) + Cloud
- **Official URL:** https://www.elastic.co/elasticsearch (docs: https://www.elastic.co/docs/)
- **Description:** Distributed inverted index + kNN dense_vector, ESQL, ILM; logs/metrics/APM stack.
- **Contents inspected:** Elastic docs (mapping, query DSL, vector search).
- **Capabilities:** BM25 + hybrid (RRF), geo, aggregations, ML.
- **Usage domain:** Product search, observability, SIEM.
- **Integration:** official clients (JS/Python/Go); Logstash/Beats/OTel
- **Compatibility:** 8.x; Lucene 9/10.
- **Deps:** JVM.
- **Availability:** Docker `elasticsearch:`; Elastic Cloud.
- **Maintenance:** Active.
- **License:** SSPL/Elastic License (not OSI) — OpenSearch is Apache fork alternative.
- **Security/limits:** X-Pack security (TLS/RBAC/API keys) must be enabled; snapshot encryption.
- **Related:** OpenSearch, Solr, Meilisearch.
- **Sources:** elastic.co/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 10 — Meilisearch + Typesense (lightweight search duo)
- **Canonical identities:** `tool:meilisearch` · `tool:typesense`
- **Category:** Data → Instant search
- **Type:** OSS (+ Cloud)
- **Official URLs:** https://www.meilisearch.com/ (docs: https://www.meilisearch.com/docs) · https://typesense.org/ (docs: https://typesense.org/docs/)
- **Description:** Typo-tolerant instant search, faceting/geo/vector hybrid; simpler ops than ES; instantsearch adapters.
- **Contents inspected:** Both docs (quickstart, API, hybrid search).
- **Capabilities:** Synonyms, ranking rules, multi-search, scoped API keys.
- **Usage domain:** Storefront/docs search, autocomplete.
- **Integration:** official JS/PHP/Python SDKs + InstantSearch adapters
- **Compatibility:** Single-binary/Docker.
- **Deps:** None.
- **Availability:** Docker + Cloud free tiers.
- **Maintenance:** Active (Meili v1.x; Typesense v26/27 2024-2026).
- **License:** MIT (Meili core) / GPL-3.0 (Typesense core) + Cloud ToS.
- **Security/limits:** Master key rotation; tenant tokens with filters; index PII minimization.
- **Related:** Algolia (SaaS), OpenSearch.
- **Sources:** Official docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 11 — Pinecone (managed vector) — managed exemplar
- **Canonical identity:** `saas:pinecone` — Pinecone Systems
- **Category:** Data → Vector database (managed)
- **Type:** Commercial SaaS (+ OSS clients)
- **Official URL:** https://www.pinecone.io/ (docs: https://docs.pinecone.io/)
- **Description:** Serverless/pods indexes, namespaces, metadata filtering, rerank; RAG default in many starters.
- **Contents inspected:** Pinecone docs (quickstart, data model).
- **Capabilities:** Upsert/query (cosine/dot), hybrid (sparse-dense), backups.
- **Usage domain:** Semantic search, RAG, recs.
- **Integration:** official SDKs (JS/Python/Go/LangChain/LlamaIndex)
- **Compatibility:** SaaS API; no self-host.
- **Deps:** Embedding provider (OpenAI/Cohere/etc.).
- **Availability:** Free tier + paid serverless.
- **Maintenance:** Active.
- **License:** Clients Apache-2.0; service ToS/DPA.
- **Security/limits:** API-key scoping, namespace isolation, PII in vectors is still PII.
- **Related:** Weaviate, Qdrant, pgvector (self-host alts).
- **Sources:** docs.pinecone.io.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 12 — Weaviate (vector + hybrid)
- **Canonical identity:** `tool:weaviate` — `github:weaviate/weaviate`
- **Category:** Data → Vector search engine
- **Type:** OSS (+ Cloud)
- **Official URL:** https://weaviate.io/ (docs: https://weaviate.io/developers/weaviate)
- **Description:** HNSW, modules (text2vec/ rerankers), GraphQL/REST/gRPC, multi-tenancy; generative search.
- **Contents inspected:** Weaviate developer docs.
- **Capabilities:** Hybrid BM25+vector, geo, backups, RBAC/OIDC.
- **Usage domain:** Self-host RAG, multi-tenant SaaS search.
- **Integration:** official clients + LangChain/LlamaIndex
- **Compatibility:** Docker/K8s 1.24+.
- **Deps:** None (modules optional GPU).
- **Availability:** Docker `semitechnologies/weaviate`; Cloud sandbox.
- **Maintenance:** Active (1.2x-1.3x 2024-2026).
- **License:** BSD-3-Clause (core).
- **Security/limits:** OIDC + API-key auth; module network egress review.
- **Related:** Qdrant, Milvus, pgvector.
- **Sources:** weaviate.io/developers.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 13 — Qdrant (vector, Rust)
- **Canonical identity:** `tool:qdrant` — `github:qdrant/qdrant`
- **Category:** Data → Vector engine
- **Type:** OSS (+ Cloud)
- **Official URL:** https://qdrant.tech/ (docs: https://qdrant.tech/documentation/)
- **Description:** Rust HNSW + quantization (PQ/SQ), payload indexes, distributed; strong price/perf for self-host.
- **Contents inspected:** Qdrant docs (collections/snapshots/distributed).
- **Capabilities:** Filtering, aliases, replicas/shards, sparse vectors.
- **Usage domain:** Edge/self-host RAG, recs.
- **Integration:** official JS/Python/Rust clients
- **Compatibility:** Docker/K8s.
- **Deps:** None.
- **Availability:** Docker `qdrant/qdrant`; Cloud free tier.
- **Maintenance:** Active (1.9-1.13 2024-2026).
- **License:** Apache-2.0.
- **Security/limits:** API-key + TLS; snapshot encryption at rest (volume-level).
- **Related:** Weaviate, Milvus, pgvector.
- **Sources:** qdrant.tech/documentation.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 14 — pgvector (Postgres extension) + pgx-bm25 note
- **Canonical identity:** `ext:pgvector` — `github:pgvector/pgvector`
- **Category:** Data → In-database vectors (+ BM25 via `pgx-bm25`)
- **Type:** OSS extension
- **Official URL:** https://github.com/pgvector/pgvector (docs in README; PGXN)
- **Description:** `vector` type + HNSW/IVFFlat in Postgres; 2026-10-07 news `pgx-bm25 1.0` adds native BM25 index (homepage-verified).
- **Contents inspected:** pgvector README (install/indexing); postgresql.org news item for pgx-bm25.
- **Capabilities:** `<=>` distance ops, hybrid with tsvector/BM25, RLS-joined retrieval.
- **Usage domain:** Single-DB RAG without new infra.
- **Integration:** native (`CREATE EXTENSION vector`; Drizzle/Prisma raw SQL or `drizzle-orm` pgvector helpers)
- **Compatibility:** PG 12+; Neon/Supabase/RDS support.
- **Deps:** Postgres + build tools.
- **Availability:** GitHub/PGXN/apt.
- **Maintenance:** Active (0.7/0.8 2024-2026).
- **License:** PostgreSQL License.
- **Security/limits:** Index build memory (`maintenance_work_mem`); RLS on joined docs.
- **Related:** pg_trgm, ParadeDB, Qdrant.
- **Sources:** GitHub README; postgresql.org news (WebFetch).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 15 — Prisma ORM (v5/v6 + Prisma Postgres)
- **Canonical identity:** `npm:@prisma/client` + `npm:prisma` — Prisma Data
- **Category:** Data → ORM + managed Postgres
- **Type:** OSS (core) + commercial Cloud
- **Official URL:** https://www.prisma.io/ (docs: https://www.prisma.io/docs/)
- **Description:** Declarative `schema.prisma`, typed client, Migrate/Studio; Prisma Postgres (PG 17 + pooling/cache/edge) + `create-db` CLI; comparison vs Drizzle documented.
- **Contents inspected:** WebSearch-verified Prisma docs (Postgres quickstart, Drizzle-ORM page, ORM-vs-Drizzle comparison, v6/v7 client references).
- **Capabilities:** Introspection, extensions, Accelerate caching, Pulse streams.
- **Usage domain:** TS monoliths (Next/Nuxt/Nest).
- **Integration:** official adapters (PG/neon/planetscale drivers; Auth.js adapters)
- **Compatibility:** Node 16+; TS 4.5+.
- **Deps:** Engines (Rust) downloaded postinstall.
- **Availability:** npm `prisma`.
- **Maintenance:** Active (5.x/6.x 2024-2026).
- **License:** Apache-2.0 (ORM).
- **Security/limits:** `DATABASE_URL` secret handling; connection-limit tuning; preview-feature review.
- **Related:** Drizzle, TypeORM, Kysely.
- **Sources:** Prisma docs excerpts (search session).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 16 — Drizzle ORM (+ Kit/Studio)
- **Canonical identity:** `npm:drizzle-orm` + `npm:drizzle-kit` — `github:drizzle-team/drizzle-orm`
- **Category:** Data → Lightweight TS ORM
- **Type:** OSS
- **Official URL:** https://orm.drizzle.team/ (docs: https://orm.drizzle.team/docs/)
- **Description:** SQL-like builder + relational queries; TS-schema → SQL migrations; RLS support (PG); dialect breadth (PG/MySQL/SQLite/SingleStore/Gel).
- **Contents inspected:** WebSearch-verified Drizzle docs (transactions, get-started PG, RLS, Kit 0.27-0.30 notes, Studio).
- **Capabilities:** `db.transaction`/savepoints, replicas, serverless drivers (Neon/Vercel/Supabase/Xata).
- **Usage domain:** Edge/serverless TS, thin-wrapper preference.
- **Integration:** official per-dialect imports (`drizzle-orm/neon`, `/vercel-postgres`, `/node-postgres`)
- **Compatibility:** Node 18+/edge; TS 5+.
- **Deps:** Driver (`pg`, `postgres`, `@neondatabase/serverless`).
- **Availability:** npm.
- **Maintenance:** Active (0.36-0.44 2024-2026).
- **License:** Apache-2.0.
- **Security/limits:** Raw `sql`` injection review; migration review in CI (`drizzle-kit check`).
- **Related:** Prisma, Kysely, Knex (legacy).
- **Sources:** Drizzle docs excerpts (search session).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 17 — SQLAlchemy (2.x) + Alembic
- **Canonical identities:** `pypi:SQLAlchemy` · `pypi:alembic`
- **Category:** Data → Python ORM + migrations
- **Type:** OSS
- **Official URLs:** https://www.sqlalchemy.org/ · https://alembic.sqlalchemy.org/
- **Description:** Unit-of-work ORM + Core expression language; Alembic versioned migrations; 2.0 async (`asyncpg/aiosqlite`).
- **Contents inspected:** SQLAlchemy 2.0 docs + Alembic tutorial TOC.
- **Capabilities:** Types, hybrid attrs, asyncio, reflection.
- **Usage domain:** Django-alternative Python services, FastAPI standard (`SQLModel` builds on it).
- **Integration:** official dialects (psycopg/asyncpg, aiomysql); FastAPI dependency pattern
- **Compatibility:** Python 3.8+.
- **Deps:** `greenlet` (async), DBAPI driver.
- **Availability:** PyPI.
- **Maintenance:** Active (2.0.x).
- **License:** MIT.
- **Security/limits:** Parameterize `text()`; Alembic downgrade testing.
- **Related:** Django ORM, Prisma (TS analog), Peewee/Tortoise (alts).
- **Sources:** Official docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 18 — Kysely (type-safe query builder)
- **Canonical identity:** `npm:kysely` — `github:kysely-org/kysely`
- **Category:** Data → TS SQL builder
- **Type:** OSS
- **Official URL:** https://kysely.dev/ (repo: https://github.com/kysely-org/kysely)
- **Description:** Code-first typed SQL (no decorators); dialects PG/MySQL/SQLite; Prisma-Postgres quickstart documents it.
- **Contents inspected:** kysely.dev API + Prisma Kysely-quickstart excerpt (search-verified).
- **Capabilities:** CTEs, transactions, plugins (CamelCase), migrations.
- **Usage domain:** Teams wanting SQL control + types without ORM magic.
- **Integration:** official dialects (`PostgresDialect` over `pg`)
- **Compatibility:** Node 18+; edge via adapters.
- **Deps:** Driver.
- **Availability:** npm.
- **Maintenance:** Active (0.27/0.28).
- **License:** MIT.
- **Security/limits:** Dynamic table/column names need allowlists.
- **Related:** Drizzle, Zapatos, Slonik.
- **Sources:** kysely.dev; Prisma docs mention.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 19 — Flyway (migration runner exemplar)
- **Canonical identity:** `tool:flyway` — Redgate
- **Category:** Data → Versioned migrations
- **Type:** OSS Community + Teams/Enterprise
- **Official URL:** https://flywaydb.org/ (docs: https://documentation.red-gate.com/fd)
- **Description:** SQL/Java versioned (`V1__`) + repeatable (`R__`) migrations; validate/repair/baseline; multi-DB.
- **Contents inspected:** Flyway docs (concepts, CLI).
- **Capabilities:** Checksums, callbacks, dry-run, Testcontainers testing.
- **Usage domain:** JVM/polyglot migration discipline.
- **Integration:** official (Maven/Gradle/Docker/GitHub Action)
- **Compatibility:** 20+ DBs (PG/MySQL/Oracle/MSSQL).
- **Deps:** JDBC drivers.
- **Availability:** GitHub + Docker `flyway/flyway`.
- **Maintenance:** Active (v10 2024-2026).
- **License:** Apache-2.0 (Community) / commercial (Teams+).
- **Security/limits:** Migration secrets via vault; `validateOnMigrate` in CI.
- **Related:** Liquibase, Atlas, Alembic, Prisma Migrate.
- **Sources:** flywaydb.org.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 20 — Atlas (declarative schema as code)
- **Canonical identity:** `tool:atlas` — Ariga (`github:ariga/atlas`)
- **Category:** Data → Declarative migrations/CI
- **Type:** OSS (+ Cloud)
- **Official URL:** https://atlasgo.io/ (docs: https://atlasgo.io/docs)
- **Description:** HCL/SQL desired-state, drift detection, `atlas migrate diff/apply`, GitHub Actions review.
- **Contents inspected:** Atlas docs (concepts, CLI).
- **Capabilities:** Linting, policies, Postgres/MySQL/SQLite/ClickHouse.
- **Usage domain:** GitOps DB reviews.
- **Integration:** official Action + Terraform provider
- **Compatibility:** CLI single binary.
- **Deps:** None.
- **Availability:** GitHub releases; Cloud free tier.
- **Maintenance:** Active.
- **License:** Apache-2.0 (core).
- **Security/limits:** `DATABASE_URL` in CI secrets; dev-database URL for normalization.
- **Related:** Flyway, Liquibase, Prisma Migrate.
- **Sources:** atlasgo.io.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 21 — Upstash (serverless Redis/Kafka/Vector/QStash)
- **Canonical identity:** `saas:upstash` — Upstash Inc.
- **Category:** Data → Serverless data + messaging
- **Type:** Commercial SaaS (pay-per-request)
- **Official URL:** https://upstash.com/ (docs: https://upstash.com/docs)
- **Description:** Per-request Redis/Kafka/Vector/Search/QStash (cron/webhooks) for edge/serverless; Vercel integration.
- **Contents inspected:** Upstash docs (Redis/Kafka/Vector/QStash guides).
- **Capabilities:** REST API (no persistent conn), pipelines, global replication.
- **Usage domain:** Edge caching/queues/cron without VPC.
- **Integration:** official SDKs (`@upstash/redis`, `@upstash/qstash`, `@upstash/vector`)
- **Compatibility:** HTTP-based; works everywhere.
- **Deps:** Network.
- **Availability:** Free tier + paid.
- **Maintenance:** Active.
- **License:** SDKs MIT; service ToS.
- **Security/limits:** Token scoping; request signing (QStash); PII TTLs.
- **Related:** Redis, Cloudflare KV/Queues, Inngest.
- **Sources:** upstash.com/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 22 — Amazon S3 (+ S3-compatible MinIO) — object storage exemplar
- **Canonical identities:** `saas:aws-s3` · `tool:minio` (`github:minio/minio`)
- **Category:** Data → Object storage
- **Type:** Cloud service + OSS server
- **Official URLs:** https://aws.amazon.com/s3/ · https://min.io/ (docs: https://min.io/docs/)
- **Description:** 11×9s blobs with versioning/lifecycle/presigned URLs; MinIO is S3-API self-host for dev/air-gap.
- **Contents inspected:** AWS S3 user guide TOC; MinIO docs (deploy/console).
- **Capabilities:** Multipart, SSE-KMS, Object Lock, event notifications.
- **Usage domain:** Media, backups, data lakes, static sites.
- **Integration:** open-standard API (AWS SDK v3 `S3Client`; `s3fs`, Rclone, Terraform)
- **Compatibility:** S3 API de-facto.
- **Deps:** None (MinIO single binary).
- **Availability:** AWS + Docker `minio/minio`.
- **Maintenance:** Active.
- **License:** Service ToS / MinIO AGPL-3.0 (server; commercial option).
- **Security/limits:** Block-public-access + presigned TTLs + bucket policies; SSE by default.
- **Related:** R2 (zero-egress alt), GCS, Supabase Storage.
- **Sources:** Official docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 23 — Cloudinary (media store + transforms) — media-storage exemplar
- **Canonical identity:** `saas:cloudinary` — Cloudinary Ltd
- **Category:** Data → Media storage + CDN transforms
- **Type:** Commercial SaaS (+ OSS SDKs)
- **Official URL:** https://cloudinary.com/ (docs: https://cloudinary.com/documentation)
- **Description:** Upload/store/optimize (f_auto/q_auto), eager transforms, AI cropping, video; signed uploads.
- **Contents inspected:** Cloudinary docs (upload API, transformations).
- **Capabilities:** Responsive breakpoints, background removal add-ons, DAM.
- **Usage domain:** UGC, commerce imagery, video thumbnails.
- **Integration:** official SDKs (Node/Python/PHP/Flutter)
- **Compatibility:** HTTPS APIs.
- **Deps:** Network.
- **Availability:** Free tier + paid.
- **Maintenance:** Active.
- **License:** SDKs MIT; service ToS.
- **Security/limits:** Signed presets, strict transforms (prevent fetch abuse), moderation queues.
- **Related:** Imgix, Uploadcare, S3+Image CDNs.
- **Sources:** cloudinary.com/documentation.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 24 — DuckDB (analytical embedded) — OLAP bonus
- **Canonical identity:** `tool:duckdb` — DuckDB Foundation (`github:duckdb/duckdb`)
- **Category:** Data → Embedded OLAP
- **Type:** OSS
- **Official URL:** https://duckdb.org/ (docs: https://duckdb.org/docs/)
- **Description:** In-process columnar analytics (Parquet/CSV/S3 pushdown, spatial/vector extensions); MotherDuck serverless cousin.
- **Contents inspected:** DuckDB docs (SQL, guides, WASM build).
- **Capabilities:** Window queries, `COPY TO`, Arrow zero-copy, `duckdb-wasm`.
- **Usage domain:** Local analytics, ETL previews, data-app backends.
- **Integration:** official clients (Node/Python/R/Java/WASM)
- **Compatibility:** All OSes + browser WASM.
- **Deps:** None.
- **Availability:** GitHub releases; npm `duckdb`.
- **Maintenance:** Active (0.10/1.x 2024-2026).
- **License:** MIT.
- **Security/limits:** Extension signing; untrusted DB files can carry extensions — disable autoload for untrusted inputs.
- **Related:** SQLite (OLTP cousin), ClickHouse, MotherDuck.
- **Sources:** duckdb.org/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

**Count: 24 resources** (meets 15–30 minimum). No install/execute performed.

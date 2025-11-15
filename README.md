# Data Mining

A comprehensive data mining project demonstrating various techniques and frameworks for processing large-scale data, including basic data processing, graph algorithms, recommendation systems, and big data infrastructure.

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Components](#components)
  - [Basic Data Processing](#basic-data-processing)
  - [Graph Algorithms](#graph-algorithms)
  - [Movie Recommendation Systems](#movie-recommendation-systems)
  - [Big Data Infrastructure](#big-data-infrastructure)
- [Usage Instructions](#usage-instructions)
- [Requirements](#requirements)
- [Datasets](#datasets)

## Project Overview

This repository contains implementations of various data mining techniques and algorithms, showcasing different approaches to processing and analyzing large datasets. The project covers:

- **Basic Data Processing**: Character counting, dictionary merging, and run-length encoding
- **Graph Algorithms**: PageRank implementation for analyzing web graphs and handling dead-end nodes
- **Recommendation Systems**: Multiple approaches to movie recommendation using collaborative filtering
  - Apache Spark with manual cosine similarity computation
  - Apache Spark MLlib with Alternating Least Squares (ALS)
  - MapReduce implementation using MRJob
- **Big Data Infrastructure**: HBase cluster setup using Docker Compose

The project utilizes various technologies including Python, Apache Spark, MapReduce (MRJob), and HBase, demonstrating practical applications of distributed computing frameworks for data mining tasks.

## Repository Structure

```
data-mining/
├── apache-spark/              # Apache Spark implementations
│   ├── ml-10m_similarities.ipynb      # Cosine similarity using Spark
│   ├── MLlib_ml-10m_similarities.ipynb # ALS collaborative filtering
│   └── ml-10m.zip                     # MovieLens 10M dataset
├── hbase/                     # HBase infrastructure
│   └── docker-compose-hbase.yaml      # Docker Compose configuration
├── mr-job/                    # MapReduce implementations
│   ├── MovieSimilarities.py           # MRJob movie similarity computation
│   ├── mrjob.conf                     # MRJob configuration
│   ├── rating_sample.dat              # Sample rating data
│   ├── ml-100k.zip                    # MovieLens 100K dataset
│   ├── ml-1m.zip                      # MovieLens 1M dataset
│   └── 8node-cluster-output.txt.zip   # Cluster execution output
├── count_merge.py             # Character counting and dictionary merging
├── run_length_encoding.py     # Run-length encoding implementation
├── page_rank.ipynb            # PageRank algorithm implementation
└── README.md                  # This file
```

## Components

### Basic Data Processing

#### `count_merge.py`

A Python script that demonstrates character counting and dictionary merging operations. The script:

- Reads a text file and counts characters (excluding spaces and special characters)
- Creates three random character count dictionaries by distributing characters across them
- Merges the dictionaries by summing counts
- Validates that merged counts match the original character counts

**Key Features:**

- Character frequency analysis
- Dictionary merging with validation
- Command-line interface with file path argument

#### `run_length_encoding.py`

A simple implementation of run-length encoding (RLE), a basic data compression algorithm that replaces consecutive repeated characters with a character-count pair.

**Key Features:**

- Processes input from STDIN
- Outputs compressed format: `character,count;character,count`
- Efficient for strings with many repeated characters

### Graph Algorithms

#### `page_rank.ipynb`

A Jupyter notebook implementing the PageRank algorithm using pandas and numpy. The implementation:

- Creates transition matrices from edge lists
- Computes PageRank using the power iteration method
- Handles dead-end nodes (nodes with no outgoing edges)
- Demonstrates convergence analysis

**Features:**

- Two graph examples:
  1. Simple 4-node graph (A, B, X, Y)
  2. Graph with dead-ends (Q and Z nodes)
- Iterative computation with convergence checking
- Visualization of PageRank values across iterations

### Movie Recommendation Systems

#### Apache Spark: Cosine Similarity (`apache-spark/ml-10m_similarities.ipynb`)

This notebook implements movie similarity computation using cosine similarity on the MovieLens 10M dataset with Apache Spark.

**Approach:**

- Reads ratings and movies data from S3
- Creates movie pairs rated by the same users
- Computes cosine similarity between rating vectors
- Filters results (minimum 10 co-ratings, similarity ≥ 0.95)
- Finds top 10 movies similar to "Toy Story (1995)"

**Key Operations:**

- Self-join on ratings to create movie pairs
- GroupBy aggregations for similarity components
- Cosine similarity formula: `sum(xy) / (sqrt(sum(xx)) * sqrt(sum(yy)))`

#### Apache Spark MLlib: ALS Collaborative Filtering (`apache-spark/MLlib_ml-10m_similarities.ipynb`)

This notebook uses Spark MLlib's Alternating Least Squares (ALS) algorithm for collaborative filtering.

**Approach:**

- Trains an ALS model on the MovieLens 10M dataset
- Extracts latent feature vectors (embeddings) for movies
- Computes cosine similarity between movie embeddings
- Finds top 10 movies similar to "Toy Story (1995)" based on learned features

**Key Features:**

- Matrix factorization with 50 latent features
- L2 regularization (regParam=0.1)
- Cold start strategy handling
- Embedding-based similarity computation

**Advantages over manual cosine similarity:**

- Learns hidden patterns in user preferences
- Better generalization to unseen movie pairs
- More semantically meaningful similarities (e.g., finds "Toy Story 2" as most similar)

#### MapReduce: MRJob Implementation (`mr-job/MovieSimilarities.py`)

A distributed MapReduce implementation using MRJob framework for computing movie similarities.

**MapReduce Steps:**

1. **Parse Input**: Extract userID, movieID, and rating
2. **Group by User**: Collect all ratings per user
3. **Create Pairs**: Generate all movie pairs rated by the same user
4. **Compute Similarity**: Calculate cosine similarity for each movie pair
5. **Filter & Sort**: Apply quality thresholds and sort results

**Features:**

- Multi-step MapReduce job
- Cosine similarity computation in reducer
- Quality filtering (min 10 co-ratings, similarity ≥ 0.95)
- Movie name lookup from movies.dat file
- Can run on local machine or AWS EMR cluster

**Configuration:**

- Uses `mrjob.conf` for AWS EMR credentials and region settings
- Supports distributed execution on Hadoop clusters

### Big Data Infrastructure

#### HBase Setup (`hbase/docker-compose-hbase.yaml`)

Docker Compose configuration for setting up an HBase cluster with Zookeeper.

**Components:**

- **HBase Master**: Manages cluster metadata and coordinates region servers
  - Ports: 16000 (RPC), 16010 (Web UI)
- **HBase RegionServer**: Handles data storage and retrieval
  - Ports: 16030 (Web UI), 16201, 16301 (RPC)
- **Zookeeper**: Coordinates distributed services
  - Port: 2181

**Usage:**

- Start cluster: `docker-compose -f docker-compose-hbase.yaml up`
- Access HBase Master UI: `http://localhost:16010`
- Access RegionServer UI: `http://localhost:16030`

## Usage Instructions

### Basic Data Processing

#### Running `count_merge.py`

```bash
python count_merge.py --file-path path/to/HadoopBlurb.txt
```

The script will:

1. Count characters in the file
2. Create three random character count dictionaries
3. Merge them and validate the results

#### Running `run_length_encoding.py`

```bash
echo "AAAAABBBBCCCCAA" | python run_length_encoding.py
```

Output format: `A,5;B,4;C,4;A,2`

### Graph Algorithms

#### Running `page_rank.ipynb`

1. Open the notebook in Jupyter:
   ```bash
   jupyter notebook page_rank.ipynb
   ```
2. Ensure required packages are installed: `pandas`, `numpy`
3. Run all cells to see PageRank computation for both graph examples

### Movie Recommendation Systems

#### Apache Spark Notebooks

**Prerequisites:**

- Apache Spark cluster or EMR cluster
- Access to S3 bucket with MovieLens 10M dataset
- PySpark installed

**Running the notebooks:**

1. For cosine similarity approach:

   ```bash
   # In Spark cluster or EMR notebook
   # Open: apache-spark/ml-10m_similarities.ipynb
   # Update S3 path if needed
   # Run all cells
   ```

2. For MLlib ALS approach:
   ```bash
   # In Spark cluster or EMR notebook
   # Open: apache-spark/MLlib_ml-10m_similarities.ipynb
   # Update S3 path if needed
   # Run all cells
   ```

**Note:** Both notebooks read data from S3. Update the `path` variable to point to your dataset location.

#### MapReduce with MRJob

**Local execution:**

```bash
cd mr-job
python MovieSimilarities.py --items movies.dat rating_sample.dat
```

**AWS EMR execution:**

```bash
cd mr-job
python MovieSimilarities.py -r emr --items s3://your-bucket/movies.dat s3://your-bucket/ratings.dat
```

**Configuration:**

- Update `mrjob.conf` with your AWS credentials
- Ensure IAM permissions for EMR and S3 access

### Big Data Infrastructure

#### Starting HBase Cluster

```bash
cd hbase
docker-compose -f docker-compose-hbase.yaml up -d
```

**Accessing HBase:**

- Master Web UI: http://localhost:16010
- RegionServer Web UI: http://localhost:16030
- HBase Shell: `docker exec -it <container-name> hbase shell`

**Stopping the cluster:**

```bash
docker-compose -f docker-compose-hbase.yaml down
```

## Requirements

### Python Version

- Python 3.7 or higher

### Python Packages

**Core packages:**

```bash
pip install pandas numpy
```

**For Jupyter notebooks:**

```bash
pip install jupyter notebook
```

**For Apache Spark:**

- PySpark (typically included with Spark distribution)
- Access to Spark cluster or AWS EMR

**For MapReduce:**

```bash
pip install mrjob
```

**For HBase:**

- Docker and Docker Compose

### System Requirements

- **For Spark notebooks**: Access to Spark cluster (local, standalone, or AWS EMR)
- **For MRJob on EMR**: AWS account with EMR permissions
- **For HBase**: Docker installed and running

### Optional Dependencies

- AWS CLI (for S3 access)
- Hadoop (for local MapReduce execution)

## Datasets

### MovieLens Datasets

The project uses MovieLens datasets for recommendation system implementations:

- **MovieLens 100K** (`mr-job/ml-100k.zip`): 100,000 ratings from 943 users on 1,682 movies
- **MovieLens 1M** (`mr-job/ml-1m.zip`): 1 million ratings from 6,040 users on 3,900 movies
- **MovieLens 10M** (`apache-spark/ml-10m.zip`): 10 million ratings from 71,567 users on 10,681 movies

**Dataset Format:**

- `ratings.dat`: `UserID::MovieID::Rating::Timestamp`
- `movies.dat`: `MovieID::Title::Genres`

**Note:** The Spark notebooks read data from S3. For local execution, extract the zip files and update the path in the notebooks.

### Other Data

- `mr-job/rating_sample.dat`: Sample rating data for testing MRJob locally
- `mr-job/8node-cluster-output.txt.zip`: Output from 8-node cluster execution (for reference)

---

## License

This project is for educational purposes, demonstrating various data mining techniques and distributed computing frameworks.

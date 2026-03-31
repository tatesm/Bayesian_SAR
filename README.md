# 🛰️ Bayesian Search and Rescue (SAR) Simulation

## Overview

This project implements a **Bayesian Search and Rescue (SAR) model** that simulates how search teams locate a missing person or object under uncertainty.

The system maintains a **probability distribution over a search area**, updates that distribution after each search, and prioritizes future searches to maximize the likelihood of success.

---

## Core Concepts

### 1. Probability of Area (POA)

The search space is divided into a grid. Each cell contains a probability representing the likelihood that the target is located there.

- All probabilities sum to **1.0**
- The initial distribution (prior) is based on:
  - Last known position
  - Terrain features
  - Behavioral assumptions

---

### 2. Probability of Detection (POD)

POD represents the probability of detecting the target **given that it is in a searched area**.

POD depends on:
- Terrain (forest, open ground, etc.)
- Search method (ground team, drone, etc.)
- Search coverage

> Important: Even if a location is searched, the target may not be detected.

---

### 3. Probability of Success (POS)

\[
POS = POA × POD
\]

This is the **primary decision metric** used to allocate search effort.

- High POA but low POD → not ideal  
- High POD but low POA → not ideal  
- Highest POS → best search candidate  

---

### 4. Search Effort and Coverage

Search effort quantifies how much area is effectively searched:

\[
Z = W × L
\]

- \( W \): sweep width  
- \( L \): distance traveled  

Coverage is defined as:

\[
Coverage = \frac{Effort}{Area}
\]

Higher coverage increases the probability of detection.

---

### 5. Bayesian Updating

After searching an area:

- If the target is not found, probability in that area is **reduced based on POD**
- The remaining probability is **renormalized across the grid**

> Crucially, searched areas are **not reduced to zero**, since detection is imperfect.

This updating process is repeated iteratively as new searches are conducted.

---

## Core Algorithm Loop

1. Initialize probability map (POA)  
2. Select search region based on highest POS  
3. Simulate search using POD  
4. Update probability distribution  
5. Repeat  

---

## Project Roadmap

### Phase 1 – MVP
- Grid-based probability map  
- Gaussian prior around last known location  
- Constant or simple POD model  
- Bayesian update after search  

**Outputs:**
- Probability heatmap  
- Search path selection  

---

### Phase 2 – Enhanced Model
- Terrain-based probability weighting  
- Movement model (Markov transitions)  
- Variable POD based on conditions  
- Multiple search units  

---

### Phase 3 – Advanced System
- Monte Carlo particle simulation (SAROPS-inspired)  
- Time-evolving probability distributions  
- Integration with real GIS data  
- Optimization of search allocation strategies  

---

## Goal

This project demonstrates:

- Bayesian reasoning under uncertainty  
- Simulation-based modeling  
- Decision-making optimization  
- Real-world application of statistical methods  

---
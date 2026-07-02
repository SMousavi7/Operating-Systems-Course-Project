# Operating Systems Course Project – Memory Management Simulation

This repository contains a pilot implementation of an Operating Systems course project designed and developed by **[Your Name]** and **[Friend's Name]**.

The main goal of this project is to simulate and analyze concepts related to memory management in operating systems, especially page allocation, page faults, CPU execution, threads, files, and MMU behavior.

## Project Overview

In this project, we designed a simplified operating-system-like environment to study how different memory configurations can affect system behavior.

The current implementation focuses on a simulation where multiple files and threads are created, and the CPU interacts with the MMU to execute them. During the simulation, the number of page faults is measured for different page sizes.

This version should be considered a **pilot implementation**. It represents the initial experimental version of the idea and can be extended into a more complete operating system simulator.

## Main Components

The project is built around the following core components:

* `CPU`: Simulates the execution unit and manages threads.
* `MMU`: Simulates memory management and tracks page faults.
* `Thread`: Represents executable units inside the simulation.
* `File`: Represents files with memory ranges.
* Simulation script: Runs experiments using different page sizes and collects results.

## Experiment

The pilot experiment tests how changing the page size affects the number of page faults.

The simulation uses:

* 100 generated files
* 20 generated threads
* Multiple page sizes
* 25 simulation rounds for each page size

For each page size, the program calculates the average number of page faults and generates visual outputs.

## Outputs

The project generates visual results to help analyze the simulation behavior.

Generated outputs include:

* Histograms of page fault counts for each page size
* A final comparison chart showing the mean number of page faults for different page sizes

Example output files:

```text
pagefaults_histogram1.png
pagefaults_histogram2.png
pagefaults_histogram4.png
...
mean_pagefaults_vs_page_sizes.png
```

## Running the Project

Install the required dependencies:

```bash
pip install numpy matplotlib
```

Then run the simulation:

```bash
python main.py
```

If the project is used inside a Jupyter Notebook, the plots can also be displayed directly inside the notebook while still being saved as image files.

## Educational Purpose

This project was created for educational purposes as part of an Operating Systems course. It is intended to demonstrate memory management concepts through simulation and experimentation.

The current code is not meant to be a production-level simulator, but rather a pilot version for testing the core idea and visualizing the results.

## Authors

Designed and developed by:

* **[Your Name]**
* **[Friend's Name]**

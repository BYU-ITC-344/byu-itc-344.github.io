---
title: Lab 2 - Containers
---
# Lab 2 - Containers

## Introduction

You have already had some exposure to virtualization in the last lab. This lab aims to strengthen your understanding of containerization. In this lab you will learn about two forms of containerization: operating system containers, and application containers.

### Containers

As a review, A container virtualizes the operating system but does not virualize hardware. It shares the kernel of the host. Containers are smaller and lighter-weight than VMs, and they can start up faster and use fewer system resources. Multiple containers can run on the same host system, and each container shares the host's operating system kernel.

### Operating System Containers

Operating system containers allow another operating system to use the host kernel. These kind of containers are general purpose, meaning you can interact with them like you would a regular OS. They come with a file system and terminal. LXC containers are open source linux containers. The templates to create LXC containers are included in most Linux distros.

### Application Containers

Application containers like Docker are designed to virtualize services for particular applications. Application containers include an operating system, but the OS is only a vehicle for the intended application. Application containers are valuable because they make a service avaliable and portable. 


## Lab Technologies

After this lab, you will have worked installed or worked with

- Operating System Container

- Application Container
    - Docker Desktop
    - Docker Hub


<div style="page-break-after: always"></div>

## Instructions

Your supervisor has asked you to prepare a lightweight **testing environment in Proxmox** for the company’s new website. In production, websites are deployed as Docker images. For this testing phase, however, you are expected to:

1. **Set up an unprivileged LXC container** in Proxmox (for added security).
1. **Install Docker** inside the container.
1. **Build a Docker image** for the new website.
1. **Document the process** so that other team members can follow it in the future.

The development team has provided you with the **website source code** (see: <a href="lab2SiteSource.zip" download>Lab2SiteSource.zip</a>) and noted that the application requires the Python libraries **Flask** and **python-dotenv**.


## Reference Material

Before departing, the previous Docker engineer left the following guidance:

> ### Understanding the Fundamentals of Docker
>
> Docker is a platform for packaging and deploying web servers and other services in a **portable and reproducible** way.
>
> - **Docker Containers** are the end goal. They are running instances of services, isolated within a lightweight operating system environment. Containers can be created, started, stopped, or deleted.
> - **Docker Images** are templates used to create containers. Images define the base OS and tools available inside the container. Many prebuilt images are hosted on <a href="https://hub.docker.com" target="_blank">Docker Hub</a>, where you can also upload your own.
> - **Dockerfiles** allow you to build custom images. They define the base image, installed software, configurations, and any commands that need to be executed.
> - **Docker Compose files (YAML)** provide a way to manage multi-container applications. They can define how images are built (using Dockerfiles), configure services, and control deployment without long command-line arguments.

This document will serve as a reference as you build the image for the new site.

## Deliverables

1. A functioning **unprivileged LXC container** in Proxmox running Docker.
1. A **Docker image** containing the provided website source code with Flask and dotenv installed.
1. Documentation of the steps taken to build and deploy the image.


### Step 1: Install a Linux Container on Proxmox

Proxmox supports **LXC containers**, which you can install directly from available templates. Review the <a href="https://pve.proxmox.com/wiki/Linux_Container#pct_container_images" target="_blank">official Proxmox LXC documentation</a> before starting.

#### Instructions

1. **Download a Container Template**

   - In the Proxmox web GUI, go to `Labs > CT Templates > Templates`
   - Select and download the container template of your choice.

1. **Create the Container**

   - Use the downloaded template to create a new LXC container.
   - Use an `Unprivileged container`
   - Configure basic settings (hostname, resources, network).

1. **Install Docker**

   - Once the container is running, install Docker inside it.
   - The exact package depends on your chosen operating system. Refer to the following resources for guidance:
      - <a href="https://octopus.com/blog/difference-between-docker-versions#:~:text=The%20docker.io%20and%20docker,a%20package%20provided%20by%20Docker" target="_blank">Difference between docker.io and docker-ce</a>
      - <a href="https://superuser.com/questions/784258/whats-the-difference-between-docker-io-and-docker" target="_blank">SuperUser: Difference between docker.io and docker</a>


1. **Test Docker**

   - Run the following command to confirm Docker is installed and working:

     ```sh
     docker run hello-world
     ```

   - Optionally, test by running an Apache server on port 80:

     ```sh
     docker run -d --name my-apache-app -p 80:80 httpd:latest
     ```

### Step 2: Create a Docker Container

This step will be done on your **personal machine** before moving back into the Proxmox environment. You’ll build and run a Docker container for a simple website, then upload it to DockerHub for use in your LXC container.

For reference, review the official Docker <a href="https://docs.docker.com/compose/gettingstarted/" target="_blank">Getting Started with Compose Guide</a>.

#### General Tips

- The **terminal** is your best friend.
- Your website will run on **HTTP**, not HTTPS.
- You can specify which **port** your container uses.
- Some commands may require **sudo** privileges.
- Take **notes** on your process (Steps 2.2 – 2.4).
- On **macOS**, Docker Desktop builds images with **ARM64 architecture**. For compatibility, build your final container on a **VM (x86-64)**.

### Step 2.1 – Install Docker

1. Install **Docker Desktop** on your local machine.
1. Verify your installation by running:

   ```sh
   docker run hello-world
   ```
### Step 2.2 – Create a Dockerfile

1. Create a `Dockerfile` for your project.
1. Use the <a href="https://docs.docker.com/compose/gettingstarted/" target="_blank">Compose Getting Started Guide</a> as a reference.
1. Adapt the example to meet the **specifications from your web development team**.

### Step 2.3 – Build an Image from the Dockerfile

1. Use Docker commands to build your image
1. Verify the image exists

### Step 2.4 – Create and Run a Container from Your Image

1. Run your container using either:

   - **Docker CLI** (`docker run`)
   - or a **Docker Compose file** (`docker-compose up`)

1. Verify that:

   - The container is running in **Docker Desktop**
   - The website is accessible in your **browser**

1. Take a screenshot showing both:

   - Docker Desktop with the columns `Name`, `Image`, `Status`, `Port(s)`
   - Your browser displaying the running website with the **port number** visible

   Example:
   ![working-image-and-container](example.png){: style="display: block; width: 90%; margin: 0 auto; padding: 0.5em; border: 1px solid #808080;" }


### Step 3 – Upload Your Image to DockerHub

1. Create a **DockerHub account** (if you don’t already have one).
1. Tag and push your image to DockerHub:

   ```sh
   docker tag my-web-image username/my-web-image
   docker push username/my-web-image
   ```
1. Take a screenshot of your image as it appears on **DockerHub**.


### Step 4 – Pull Your Image and Run It in the Linux Container

1. In your **Proxmox LXC container**, pull down the image:
1. Run the container 
1. Verify the container is running and accessible.
    - You will need to use one of your VMs with a GUI from lab 1 to verify this


### Step 5 – Write Up

You must complete a **write-up** of your work using the provided template. The write-up should include:

- **Answers to all questions**
- **Screenshots for each of the following:**
  1. A running LXC with network information displayed (Step 1)
  1. A running LXC with the `hello-world` Docker container running (Step 1)
  1. Docker Desktop installed on your computer (Step 2.1)
  1. The Dockerfile used in Step 2.2
  1. The commands you used to create and verify the Docker image (Step 2.3)
  1. The Docker image running in Docker Desktop (Step 2.4)
  1. Your website accessible in a browser (Step 2.4)
  1. The Docker image uploaded to DockerHub (Step 3)
  1. Pulling down your Docker image on the LXC container (Step 4)
  1. Running your container in the LXC container (Step 4)
  1. Your container working in a browser from the LXC container (Step 4)

#### Templates

- <a href="lab-2-writeup-template.docx)" download>Download the MS Word Write-Up Template (.docx)</a>
- <a href="lab-2-writeup-template.mdp" download>Download the Markdown Write-Up Template (.md)</a>

## Helpful links

<a href="https://www.dataset.com/blog/create-docker-image/" target="_blank">Creating and managing a Docker Image</a>

<a href="https://docs.docker.com/get-started/02_our_app/" target="_blank">Contains information on how to use a Dockerfile</a>

<a href="https://docs.docker.com/develop/develop-images/dockerfile_best-practices/" target="_blank">Dockerfile syntax and best practices</a>

<a href="https://docs.docker.com/compose/gettingstarted/" target="_blank">How docker compose can be used to create a docker image and information on how to create a Dockerfile</a>


### Requirements and Points

### Grading Breakdown (100 Points Total)


| **Task**                                                               | **Points** |
| ---------------------------------------------------------------------- | ---------- |
| A running LXC with network information displayed (Step 1)              | 10         |
| A running LXC with the `hello-world` Docker container running (Step 1) | 5          |
| Docker Desktop installed on your computer (Step 2.1)                   | 10         |
| A working Dockerfile                                                   | 10         |
| The commands you used to create and verify the Docker image (Step 2.3) | 5          |
| The Docker image running in Docker Desktop (Step 2.4)                  | 10         |
| Your website accessible in a browser (Step 2.4)                        | 5          |
| The Docker image uploaded to DockerHub (Step 3)                        | 10         |
| Pulling down your Docker image on the LXC container (Step 4)           | 5          |
| Running your container in the LXC container (Step 4)                   | 5          |
| Your container working in a browser from the LXC container (Step 4)    | 5          |
| Write-Up Questions                                                     | 20         |


## Submission
Create a single PDF from the given `Write Up` file that contains your written report and screenshots showing that each requirement has been met. Upload the PDF to Learning Suite. Any other file format will not be accepted.
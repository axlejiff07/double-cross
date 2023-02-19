# double-cross

FastAPI framework

# Server side programming for creating an app on retail

# Python 3, Swagger UI, PostgreSQL - to be used

# Modules to cover

- Login
- Signup
- Products
- All User details(Admin view)
- Purchase
- Order
- Payment
- Review
- User profile
- App Settings
- App utilities

# Purpose

- Learn web app development using FastAPI framework, networking for web app, third party integrations,
  REST API development, Postgresql & other advanced database handling, Use of UI frameworks like React and Angular.
  
- Other Prospective techstack to be used: terraform, docker, redis cache, kafka, elasticsearch, github-actions

# Prerequisites

- Knowledge of web app development using python 3
- Object relational database like Postgresql & SQL querying
- UI frameworks - React, Angular or Vue.js (May learn eventually by exploring as per requirements)
- OOPs concept like class, object, interface, inheritance, data encapsulation.
- Data structures like Array, Dictionary, Sets, Map, Queue. Advance level -> Stack, HashMap, Graph
- Networking basics - protocols like HTTP, SMTP, FTP. Subnets, VPC, Firewalls. Advance level -> WebRTC, RTMP for streaming
- SDE design and architecture

# Installation

- pip install "fastapi[all]"


# Instructions for testing the code

Step 1: https://fastapi.tiangolo.com/tutorial/first-steps/

Step 2: https://fastapi.tiangolo.com/tutorial/path-params/

# Git & coding paradigms to be followed

- Commit message format:
  - [add]: File, function, service, variable, or data added
  - [mod]: File, function, service, variable, or data modified
  - [rename]: File, function, service, variable, or data renamed
  - [del]: File, function, service, variable, or data deleted or replaced
  - [merge]: Branch, commits or code merged
  - [test]: Test cases for xyz feature added
  - [readme]: Readme file updated
  - [lint]: Files formatted with xyz linter
  
  **In case of two different types of commits like [add] and [mod], choose the topmost type from above vertical list. In this case, [add] is above [mod] so choose that commit message.
  ** One commit should have one job, i.e., apply atomicity.

- Git branching format:
  - Branch name: feature-issuenumber-type
    - feature: Module name or feature name, in case of merge branch use only MERGING
    - issue number: Generated ISSUE_ID, in case of merge branch use only MERGE_ID
    - type: [Bug, dev, temp], in case of merge branch use only temp
    ** Issue number should be generated and stored in environment based branching files

  - Merging:
    - First the feature branches should be up to date with the main branch
    - Use rebase only if you can handle conflicts, otherwise use git merge with above mentioned [merge] commit messages.
    - Merge branch concept: Feature branches should be merged for testing multiple sub branches in dev server or developer instance deployment
    - Only reviewed and approved feature branches in Merge branches can be merged in Main branch
    - Only Main branch is deployed in prod server.

- Use Python VS code extension: https://marketplace.visualstudio.com/items?itemName=ms-python.python
- Use markdownlint extension: https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint
- Use docstrings for documentation: VS code extension: https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

    """_summary_

    :return: _description_
    :rtype: _type_
    """

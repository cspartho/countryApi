# Country API


## Installation

### Prerequisites

#### Install Python

Install ```python-3.7.2``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)


### If you already have Python and pip, you can easily install Pipenv into your home directory:
```bash
$ pip install --user pipenv
```
### clone the repository to your local machine:

```bash
git clone https://github.com/cspartho/countryApi.git
```
### Install requirements
```bash
cd /countryApi
pipenv install
```
### Activate virtualenvironment
```bash
pipenv shell
```
### Create the database:
```bash
python manage.py migrate
```
Finally, run the development server:

```bash
python manage.py runserver
```
The project will be available at **127.0.0.1:8000**.

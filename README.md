# acme employees pay

## Prerequisites

- Python version 3.8

## Solution overview
The program is made up of different modules, a main administration module "manage_payments", which contains the main function and it is in charge of controlling the flow of the program.

The program is also constituted by a module for the management of the inputs and outputs "manage_io", which is responsible for loading the data from a text file, then validate these data to ensure that they are correct and finally are split to be sent to the next phase, this module also contains the functions that are responsible for printing on the console the results of the execution of the program.

The module where the calculations are made is called "employee", this contains the Employee class, this class contains the functions to calculate the payment of each employee, the function "calculatePayment" is the one in charge of making the payment, in this case it was decided to create the Employee class since this will allow later to add new functionalities.

The calculated value to be paid is calculated at different time intervals but there are some restrictions.

### Restrictions:
There is a restriction on the time ranges:

If initial data of the problem is "RENE=MO22:00-20:00"
It generates an "out hours" error, because this would mean that the employee worked more than 24 hours, 
which is not allowed, in this case the data is not computed, but the remaining information is computed, at the end the user is warned in console with the message:

"The amount to pay MARIA is: 55.0 USD, over hours error in some day"

## Architecture
The type of architecture used is pipeline, for this case it is sufficient 
because based on certain information, we must validate it, 
transform it, calculate a result and display the result.
1. The first step is to extract the information from a text file.
2. The second step consists of validating the information.
3. The third step consists of transforming the information
4. The fourth step consists of making the respective calculations.
5. In the fifth step the employee's information is saved in a list.
6. In the sixth step the result or errors are displayed.

<div class="figure"> <img src="https://user-images.githubusercontent.com/55673344/111832785-37ba0100-88bf-11eb-8760-86f4e9987fc7.png" alt="drawing" width="600"/></div>
<p></p> 
The first, second and sixth steps are performed in the module "manage_io", 
for simplicity only one module was used in this case. 
If the program increases in complexity it is possible to have only one module
for inputs, outputs and validation.

In the Employee class the transformation and the respective calculations 
are performed, which corresponds to the third and fourth step.

The fifth step was poorly implemented because in the statement there was no requirement to save the results, it was added for future expansion, now we simply save the instances of Employee in a list as a reference.

## Approach and methodology

The methodology used in this project focuses on the functionality of the program, the first approach was to create a functional portotype, which was improved iteratively.
It could be said that it is a lean methodology because of the limited resources, in this case "time", because this methodology seeks efficiency, which describes the approach taken at the beginning. It can also be said that it is an agile methodology since it takes into account the iteration and the fast delivery of a functional product, although in this methodology the work of multidisciplinary teams is weighted, which is not the case here. 
At the beginning a small plan was designed, it was determined that for this project a pipeline architecture was going to be used since in my opinion it is the one that best fits this problem, it was raised due to the requirements of the input phase problem and the need to validate the information.
At the beginning, I did not think of using classes since there are other ways to solve the problem just as valid, but I used this approach in the Employee class thinking in future improvements of the program since more information can be added to each instance of the class, making its management simpler.
The last stage in the development was testing, which was developed with unittest, due to the errors evidenced by this stage some improvements were made in the code to solve them.

## Usage
python manage_payments.py

test:
python -m unittest test.test_manageio.TestManageio



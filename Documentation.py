def introduction(argument1):
    """Summary or Description of the Function
    Parameters:
    An introduction.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(introduction.__doc__)
def theory(argument1):
    """Summary or Description of the Function
    Parameters:
    A theory.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(theory.__doc__)
def objective(argument1):
    """Summary or Description of the Function
    Parameters:
    An objective.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(objective.__doc__)
def experiment(argument1):
    """Summary or Description of the Function
    Parameters:
    An experiment.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(experiment.__doc__)
def quizzes(argument1):
    """Summary or Description of the Function
    Parameters:
    A quizzes.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(quizzes.__doc__)
def procedure(argument1):
    """Summary or Description of the Function
    Parameters:
    A procedure.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(procedure.__doc__)
def readings(argument1):
    """Summary or Description of the Function
    Parameters:
    A readings.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(readings.__doc__)
def List_Of_Experiments(argument1):
    """Summary or Description of the Function
    Parameters:
    An List_Of_Experiments.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(List_Of_Experiments.__doc__)
def Target_audience(argument1):
    """Summary or Description of the Function
    Parameters:
    An Target Audience.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(Target_audience.__doc__)
def faq(argument1):
    """Summary or Description of the Function
    Parameters:
    An faq.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(faq.__doc__)
def form_exp1(argument1):
    """Summary or Description of the Function
    Parameters:
    An quiz post request
    Takes the parameters sent by AJAX request through request.form
    If all inputs are valid ,fetch data from sql database created in the file
    If fetch not successful then alert user with message otherwise returns data
    """
    return jsonify({'sucess' : 'Response has been recorded'})
print(form_exp1.__doc__)

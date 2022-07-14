from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User




@app.route('/')
def index():

    users = User.get_all_users()

    return render_template('read_all.html', users=users)



@app.route('/users/create', methods=['POST'])
def create_new():
    # get the form data and puts into a dict to add to database
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    # this takes the data passed thru the form and adds it to the database. using the User class with a create_new method
    # for some reason this returns the id of the user that all so i just passed it to the redirect route to display the show page
    user_id = User.create_new(data)
    

    return redirect(f'/users/{user_id}/show')



@app.route('/users/new')
def add_new():
    return render_template('create.html')

    

@app.route('/users/<int:user_id>/show')
def show(user_id):

    data = {
        'id':user_id
    }
    user_to_show = User.get_one_user(data)

    
    # had to use index here because in the .get_one_user if i created a list of objects it wouldnt render so had to use the list of dicts and index to the one item in the list 
    return render_template('/read_one.html', user=user_to_show[0]) 



@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    
    data = {
        'id':user_id
    }

    user_to_edit = User.get_one_user(data)
    return render_template('edit.html', user=user_to_edit[0])




@app.route('/users/<int:user_id>/update', methods=['POST'])
def update(user_id):
    
    data = {
        'id':user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.update_user(data)
    

    return redirect(f'/users/{user_id}/show')


@app.route('/users/<int:user_id>/delete')
def delete(user_id):
    
    data = {
        'id':user_id,
    }

    User.delete_user(data)

    return redirect('/')
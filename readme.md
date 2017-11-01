Instructions to Create a Heroku Web Application

#These following instructions are designed for Mac#

1. Open Terminal application. Install the Heroku CLI (Command Line Interface).This can be done by running `brew install heroku/brew/heroku`, or by downloading the package [here](https://cli-assets.heroku.com/heroku-cli/channels/stable/heroku-cli.pkg).
2. Create a Heroku.com account with your email.
3. Go back to your Terminal and run `heroku login`. Enter your Heroku email and password. Be sure you have authenticated your account by clicking the link sent to your email.
4. In Terminal, type `cd Desktop` and press Enter. Then type `git clone https://github.com/alexanderldavis/....git`. Once this completes, type `cd [nameoffolder]`.
5. Still in Terminal, type `heroku create`. This will add a Heroku git remote you can use to upload your code to the internet! You're almost done!
Note:
Retain the URLs the above command prints to the screen. This should look like this:
```
http://lit-bastion-5032.herokuapp.com/ | https://git.heroku.com/lit-bastion-5032.git
Git remote heroku added
```
Copy paste this and save it in a folder, or write them down.
6. Finally, in Terminal type `git add .`, `git commit -m "Initial Commit"`, `git push heroku master`. Once this completes, move to the next step.
7. To scale your web app, run `heroku ps:scale web=1`. Now, visit in your browser the URL you wrote down earlier. To look extra cool, you can also run `heroku open` from your Terminal.

If all has gone well so far, you should see a neat webpage with the word "SUCCESS!" on it.
Nicely done! You have created your first web app. If you are using this template for the CSS Hackathon 2017, you can feel free to use this template to work on your app. It contains different elements you might want to use for

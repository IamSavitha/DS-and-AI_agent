const express = require('express');
const router = express.Router();
const bcrypt = require('bcryptjs');

// Dummy user data (for demo purposes)
const users = [
    {
        id: 1,
        username: 'admin',
        password: bcrypt.hashSync('password', 8)
    }
];

// Login route
router.get('/login', (req, res) => {
    res.render('login');
});

router.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(u => u.username === username);
    if (user && bcrypt.compareSync(password, user.password)) {
        req.session.user = user;
        res.redirect('/dashboard');
    } else {
        res.redirect('/auth/login');
    }
});

// Logout route
router.get('/logout', (req, res) => {
    req.session.destroy(err => {
        if (err) {
            return res.redirect('/dashboard');
        }
        res.redirect('/');
    });
});

module.exports = router;
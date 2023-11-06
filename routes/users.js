const express = require("express");
const router = express.Router();
const User = require("../models/users");

//Get All
router.get("/", async (req, res) => {
    try {
        const users = await User.find();
        res.json(users);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

//Login
router.get("/login", async (req, res) => {
    try {
        var user = await User.findOne({
            usuario: req.body.usuario,
            clave: req.body.clave,
        });
        if (user == null) {
            res.status(400).json({ message: "Credenciales incorrectas" });
        } else {
            res.json(user._id);
        }
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Get One
router.get("/:id", getUser, (req, res) => {
    res.json(res.flight);
});

//Create One
router.post("/", async (req, res) => {
    //Create new flight object
    //console.log(req.body);
    const user = new User({
        usuario: req.body.usuario,
        clave: req.body.clave,
        rol: req.body.rol,
    });

    try {
        const newUser = await user.save();
        res.status(201).json(newUser._id);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//Update One
router.patch("/:id", getUser, async (req, res) => {
    //check all required fields

    if (req.body.usuario != null) {
        res.user.usuario = req.body.usuario;
    }
    if (req.body.clave != null) {
        res.user.clave = req.body.clave;
    }
    if (req.body.rol != null) {
        res.user.rol = req.body.rol;
    }

    try {
        const updatedUser = await res.user.save();
        res.json(updatedUser);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//Delete One
router.delete("/:id", getUser, async (req, res) => {
    try {
        await res.user.deleteOne();
        res.json({ message: "Deleted User" });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

async function getUser(req, res, next) {
    let user;
    try {
        user = await User.findById(req.params.id);
        if (user == null) {
            return res.status(404).json({ message: "Cannot find flight" });
        }
    } catch (err) {
        return res.status(500).json({ message: err.message });
    }
    res.user = user;
    next();
}

module.exports = router;

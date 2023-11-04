const express = require("express");
const router = express.Router();
const Flight = require("../models/flights");

//Get All
router.get("/", async (req, res) => {
    try {
        const flights = await Flight.find();
        res.json(flights);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Get One
router.get("/:id", (req, res) => {
    res.send(req.params.id);
});

//Create One
router.post("/", async (req, res) => {
    //Create new flight object
    console.log(req.body);
    const flight = new Flight({
        nombre: req.body.nombre,
        puesto: req.body.puesto,
        departamento: req.body.departamento,
        internacional: req.body.internacional,
        pais: req.body.pais,
        motivo: req.body.motivo,
        fechas: req.body.fechas,
        details: req.body.details,
        alojamiento: req.body.alojamiento,
        requiere_transporte: req.body.requiere_transporte,
        estado: req.body.estado,
    });

    try {
        const newFlight = await flight.save();
        res.status(201).json(newFlight);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//Update One
router.patch("/:id", (req, res) => {});

//Delete One
router.delete("/:id", (req, res) => {});

module.exports = router;

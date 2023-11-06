const express = require("express");
const router = express.Router();
const Flight = require("../models/flights");
const User = require("../models/users");

//Get All Flights
router.get("/", async (req, res) => {
    try {
        const flights = await Flight.find();
        res.json(flights);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Get One Flight by his flght id
router.get("/:id", getFlight, (req, res) => {
    res.json(res.flight);
});

//Get all pending flight requests from an user ID
router.get("/getPendingFlights/:id", getUser, async (req, res) => {
    try {
        //Check if user id Admin
        console.log(res.user);
        if (res.user.rol == "Admin") {
            const pendingFlights = await Flight.find({
                estado: "Pendiente",
            }).select({ _id: 1, estado: 1 });
            res.json(pendingFlights);
        } else {
            res.status(403).json({ message: "Access Denied" });
        }
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//Get flights from user by his ID
router.get("/getCollaboratorFlights/:id", getUser, async (req, res) => {
    try {
        //Check if user id Admin
        console.log(res.user);
        if (res.user.rol == "Colaborador") {
            console.log(req.params.id);
            const colabFlights = await Flight.find({
                id_colaborador: req.params.id,
            });
            res.json(colabFlights);
        } else {
            res.status(403).json({ message: "Access Denied" });
        }
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//Get flights from an specific date, :id is the id of the user making the request
router.get("/getProgrammedFlights/:id", getUser, async (req, res) => {
    try {
        //Check if user id Admin
        console.log(res.user);
        if (res.user.rol == "Admin") {
            console.log(req.body.fecha);

            //Obtener datos de la fecha

            var date = new Date(req.body.fecha);

            const month = date.getMonth();
            const year = date.getFullYear();
            const startDate = new Date(year, month, 1);
            const endDate = new Date(year, month, 30);

            console.log("Fecha inicio" + startDate);
            console.log("Fecha Final" + endDate);

            const dateFlights = await Flight.find({
                "fechas.fecha_ida": {
                    $gte: startDate,
                    $lte: endDate,
                },
                estado: "Aprobado",
            }).select({
                nombre: 1,
                departamento: 1,
            });
            console.log(dateFlights);
            res.json(dateFlights);
        } else {
            res.status(403).json({ message: "Access Denied" });
        }
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//Get flights from an specific trimester and year, :id is the id of the user making the request
router.get("/getInternationalFlights/:id", getUser, async (req, res) => {
    try {
        //Check if user id Admin
        console.log(res.user);
        if (res.user.rol == "Admin") {
            //console.log(req.body.fecha);

            //Obtener datos de la fecha
            let mes;

            //Trimestre
            switch (req.body.trimestre) {
                case "1":
                    mes = 1;
                    break;
                case "2":
                    mes = 4;
                    break;
                case "3":
                    mes = 7;
                    break;
                case "4":
                    mes = 10;
                    break;
                default:
                    mes = 1;
            }

            const fecha = req.body.anho + mes + "1";

            var date = new Date(fecha);

            const month = date.getMonth();
            const year = date.getFullYear();
            const startDate = new Date(req.body.anho, mes, 1);
            const endDate = new Date(req.body.anho, mes + 2, 30);

            console.log("Fecha inicio" + startDate);
            console.log("Fecha Final" + endDate);

            const dateFlights = await Flight.find({
                "fechas.fecha_ida": {
                    $gte: startDate,
                    $lte: endDate,
                },
                internacional: true,
            }).select({
                nombre: 1,
                pais: 1,
            });
            console.log(dateFlights);
            res.json(dateFlights);
        } else {
            res.status(403).json({ message: "Access Denied" });
        }
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

router.get("/getDestinyFlights/:id", getUser, async (req, res) => {
    try {
        //Check if user id Admin
        console.log(res.user);
        if (res.user.rol == "Admin") {
            console.log(req.params.id);
            const destinyFlights = await Flight.find({
                pais: req.body.destiny,
            }).select({
                nombre: 1,
                "fechas.fecha_ida": 1,
                motivo: 1,
            });
            res.json(destinyFlights);
        } else {
            res.status(403).json({ message: "Access Denied" });
        }
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//Create One flight by a user, using his ID
router.post("/:id", getUser, async (req, res) => {
    //Create new flight object
    const flight = new Flight({
        id_colaborador: req.params.id,
        usuario: req.body.usuario,
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
        //Check if user is Colaborator
        console.log(res.user);
        if (res.user.rol == "Colaborador") {
            const newFlight = await flight.save();
            res.status(201).json(newFlight._id);
        } else {
            res.status(403).json({ message: "Admin cannot register flights" });
        }
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//Update One flight, body needs id_colaborador and id_vuelo, :id is the flight id
router.patch("/:id", getFlight, async (req, res) => {
    try {
        //Get the flight
        const flight = await res.flight;

        //Get the user that made the request
        const user = await User.findById(req.body.id_colaborador);

        //Check if the change is from a collaborator
        if (user.rol != "Colaborador") {
            //Admin solo puede cambiar el estado (Pendiente, Aprobado)
            if (req.body.estado != null) {
                res.flight.estado = req.body.estado;
            }
            //res.status(403).json({ message: "No es colaborador" });
            const updatedFlight = await res.flight.save();
            res.json(updatedFlight);
        } else {
            //check all required fields

            if (req.body.usuario != null) {
                res.flight.usuario = req.body.usuario;
            }
            if (req.body.nombre != null) {
                res.flight.nombre = req.body.nombre;
            }
            if (req.body.puesto != null) {
                res.flight.puesto = req.body.puesto;
            }
            if (req.body.departamento != null) {
                res.flight.departamento = req.body.departamento;
            }
            if (req.body.internacional != null) {
                res.flight.internacional = req.body.internacional;
            }
            if (req.body.pais != null) {
                res.flight.pais = req.body.pais;
            }
            if (req.body.motivo != null) {
                res.flight.motivo = req.body.motivo;
            }
            if (req.body.fechas != null) {
                res.flight.fechas = req.body.fechas;
            }
            if (req.body.details != null) {
                res.flight.details = req.body.details;
            }
            if (req.body.alojamiento != null) {
                res.flight.alojamiento = req.body.alojamiento;
            }
            if (req.body.requiere_transporte != null) {
                res.flight.requiere_transporte = req.body.requiere_transporte;
            }

            //Check if user made a change for their flights, he cannot make changes in other collaborator's flights
            if (
                flight.id == req.body.id_vuelo &&
                flight.id_colaborador == req.body.id_colaborador
            ) {
                const updatedFlight = await res.flight.save();
                res.json(updatedFlight);
            } else {
                res.status(400).json({
                    message: "No puede cambiar vuelos de otro colaborador",
                });
            }
        }
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//Delete One flight by their flight id, body needs id_colaborador and id_vuelo as well, :id is the flight id
router.delete("/:id", getFlight, async (req, res) => {
    try {
        //Get the flight
        const flight = await res.flight;

        //Check if the change is from a collaborator
        const user = await User.findById(req.body.id_colaborador);

        if (user.rol != "Colaborador") {
            res.status(403).json({ message: "No es colaborador" });
        } else {
            //Check if user is trying to delete one of their flights
            if (flight.id == req.body.id_vuelo) {
                await res.flight.deleteOne();
                res.json({ message: "Deleted Flight" });
            } else {
                res.status(400).json({
                    message: "No puede cambiar vuelos de otro colaborador",
                });
            }
        }
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

//Function to get one flight by his ID
async function getFlight(req, res, next) {
    let flight;
    try {
        flight = await Flight.findById(req.params.id);
        if (flight == null) {
            return res.status(404).json({ message: "Cannot find flight" });
        }
    } catch (err) {
        return res.status(500).json({ message: err.message });
    }
    res.flight = flight;
    next();
}

//Function to get one user by his ID
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

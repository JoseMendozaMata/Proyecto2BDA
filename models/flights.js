const mongoose = require("mongoose");

const flightSchema = new mongoose.Schema({
    nombre: {
        type: String,
        required: true,
    },
    puesto: {
        type: String,
        required: true,
    },
    departamento: {
        type: String,
        required: true,
    },
    internacional: {
        type: Boolean,
        required: true,
    },
    pais: {
        type: String,
        required: true,
    },
    motivo: {
        type: String,
        required: true,
    },
    fechas: {
        type: {
            fecha_ida: String,
            hora_ida: String,
            fecha_vuelta: String,
            hora_vuelta: String,
        },
        required: true,
        default: {
            fecha_ida: "0-0-0",
            hora_ida: "0:00 a.m.",
            fecha_vuelta: "0-0-0",
            hora_vuelta: "0:00 a.m.",
        },
    },
    details: {
        type: {
            nombre_aerolinea: String,
            precio: Number,
        },
        required: true,
    },
    alojamiento: {
        type: String,
        required: true,
    },
    requiere_transporte: {
        type: Boolean,
        required: true,
    },
    estado: {
        type: String,
        required: true,
        default: "Pendiente",
    },
});

module.exports = mongoose.model("flight", flightSchema);

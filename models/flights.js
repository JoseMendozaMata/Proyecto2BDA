const mongoose = require("mongoose");

const flightSchema = new mongoose.Schema({
    id_colaborador: {
        type: String,
        required: true,
    },
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
            fecha_ida: Date,
            fecha_vuelta: Date,
        },
        required: true,
        default: {
            fecha_ida: "2001-1-1",
            fecha_vuelta: "2001-1-2",
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

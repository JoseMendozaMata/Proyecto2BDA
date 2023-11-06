const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
    usuario: {
        type: String,
        required: true,
    },
    clave: {
        type: String,
        required: true,
    },
    rol: {
        type: String,
        required: true,
        default: "Colaborador",
    },
});

module.exports = mongoose.model("user", userSchema);

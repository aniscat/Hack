const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const bodyParser = require('body-parser');
const { ObjectId } = require('bson');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(bodyParser.json());

const user = 'user1'
const password = 'r8E8Aw2FXriiZxZg'
const dbname = 'registro_usuarios'
const uri = `mongodb+srv://${user}:${password}@cluster0.rgawugh.mongodb.net/${dbname}?retryWrites=true&w=majority&appName=Cluster0`;
// const uri = `mongodb://localhost:/5000`;

mongoose.connect(uri)

const connection = mongoose.connection;
connection.once('open', () => {
    console.log("MongoDB database connection established successfully");
});
// Definir un esquema y modelo de Mongoose
const usuarioSchema = new mongoose.Schema({
    _id:{
        type: ObjectId
    },
    nombre: {
        type: String
      },
    correo: {
        type: String
      },
    contraseña: {
        type: String
      }
});

const Item = mongoose.model('usuarios', usuarioSchema);

// Rutas
app.get('/items',  async (req, res) => {
    try {
        const items = await Item.find();
        res.json(items);
        console.log(items);
        // console.log("hola");
        // res.text(items)
    } catch (err) {
        res.status(400).send('Error al obtener los items');
    }
});

app.post('/items', async (req, res) => {
    const newItem = new Item(req.body);
    try {
        await newItem.save();
        res.status(201).send(newItem);
    } catch (err) {
        res.status(400).send('Error al crear el item');
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port: ${PORT}`);
});
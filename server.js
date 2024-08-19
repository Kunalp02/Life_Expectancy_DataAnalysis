const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

// middleware to parse json and url encoded request bodies with a size limit of 50mb.
app.use(bodyParser.json({ limit: '50mb' }));  // Adjust the limit as needed
app.use(bodyParser.urlencoded({ limit: '50mb', extended: true }));

let processedData = {};

// post endpoint to receive the processed data from python script
app.post('/api/data', (req, res) => {
    processedData = req.body;
    res.status(200).send("Data received successfully");
});

// get endpoint to show the received data
app.get('/api/data', (req, res) => {
    if (Object.keys(processedData).length == 0){
        return res.json(404).send("No data available");
    }
    res.json(processedData);
});

// app is listening on port 3000
app.listen(port, () => {
    console.log("Server started");
});
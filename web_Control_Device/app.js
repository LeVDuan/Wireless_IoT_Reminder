const express = require('express');
const { exec } = require('child_process');
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send(`
        <form action="/run" method="post">
            <label for="com">Cổng COM:</label><br>
            <input type="text" id="com" name="com"><br>
            <label for="deviceId">Device ID: </label><br>
            <input type="text" id="deviceId" name="deviceId"><br>
            <label for="vibrate">Thời gian rung:</label><br>
            <input type="text" id="vibrate" name="vibrate"><br>
            <input type="submit" value="Submit">
        </form>
    `);
});

app.post('/run', (req, res) => {
    const com = req.body.com;
    const deviceId = req.body.deviceId;
    const vibrate = req.body.vibrate;
    console.log(com + deviceId + vibrate);
    exec(`python ../cli/vibration.py -p ${com} -i ${deviceId} -v ${vibrate}`, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        res.send(`stdout: ${stdout}`);
    });
});

app.listen(port, () => {
    console.log(`server running: http://localhost:${port}`);
});

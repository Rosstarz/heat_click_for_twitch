import { spawn } from 'child_process';

export default async function Control(data){
    const args = ['src/mouse.py', data.x, data.y];
    // const python = 
    spawn('python311', args);
    // collect data from script
    // python.stdout.on('data', function (data) {
    //     console.log('Pipe data from python script ...');
    //     dataToSend = data.toString();
    // });
}
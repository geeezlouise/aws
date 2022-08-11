
const fs = require('fs');
const AWS = require('aws-sdk');

const S3 = new AWS.S3({ region: 'us-east-1' })

const upload = async () => {
    const fileContent = fs.readFileSync('test.txt');
    await S3.upload({ Bucket: 'sia-test-2', Key: 'marty/test.txt', Body: fileContent }).promise()
}

upload();

const download = async (filePath, bucketName, key) => {

    const params = {
        Bucket: bucketName,
        Key: key
    };

    const data = await S3.getObject(params).promise();
    fs.writeFileSync(filePath, data.Body.toString());
};

download('test.txt', 'siu-avb-bucket', 'test.txt');


const main = () => {
    upload();
    download('test.txt', 'siu-avb-bucket', 'test.txt');
}

main()
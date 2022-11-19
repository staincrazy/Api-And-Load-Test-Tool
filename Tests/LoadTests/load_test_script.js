import http from 'k6/http';
import {check} from 'k6';

const testTitles = ['Empty', 'Test', 'Titles'];
const testDescriptions = ['Empty', 'Test', 'Description']
const testText = ['Empty', 'test', 'texts']

export let options = {
    vus: 5,
    vusMax: 5,
    duration: "1m"
}


export default function () {
  const url = '';
  const payload = {
      'text': testText[Math.floor(Math.random() * testText.length)],
    'content_id': Math.random()*1000,
      'title':testTitles[Math.floor(Math.random()*testTitles.length)],
      'description':testDescriptions[Math.floor(Math.random()*testDescriptions.length)],
    'callback_url':'https://webhook.site/d284e774-acf8-41d9-865f-0e0a9a321afc'
  }

  const params = {
    headers: {
        'af-api-key':"<your_api_key>"
    },
  };

  let res = http.post(url, payload, params);


  const checkRes = check(res, {
      'status is 200':(r)=> r.status === 200
  });

}

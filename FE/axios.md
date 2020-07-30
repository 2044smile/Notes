### axios install
```
npm install axios
```

### example
```javascript
import axios from 'axios';

var url = 'https:/jsonplaceholder.typicode.com/users';
var data = {
    username: this.username,
    password: this.password
}

axios.post(url, data);

// 성공
.then(function(response) {
    console.log(response);
})
// 실패
.catch(function(response) {
    console.log(response);
})
```
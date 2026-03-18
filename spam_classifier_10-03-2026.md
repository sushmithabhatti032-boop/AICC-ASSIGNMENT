<!DOCTYPE html>
<html>
<head>
<title>Spam Detector</title>
<style>
body{
font-family: Arial;
text-align:center;
margin-top:100px;
}
textarea{
width:300px;
height:100px;
}
button{
padding:10px 20px;
margin-top:10px;
}
</style>
</head>

<body>

<h2>Spam Message Detector</h2>

<textarea id="message" placeholder="Enter message here"></textarea>
<br>

<button onclick="checkSpam()">Check Message</button>

<h3 id="result"></h3>

<script>
function checkSpam(){

let msg = document.getElementById("message").value.toLowerCase();

let spamWords = ["free","win","offer","click","money","prize","urgent"];

let isSpam = false;

for(let word of spamWords){
if(msg.includes(word)){
isSpam = true;
break;
}
}

if(isSpam){
document.getElementById("result").innerText="This message looks like SPAM!";
}else{
document.getElementById("result").innerText="This message looks SAFE.";
}

}
</script>

</body>
</html>
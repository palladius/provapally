<?php
    // _header.php
    session_start();
    $_SESSION['user'] = 'foo';
?>

<div class='header'>
Welcome to PHP Test
[

  <a href='/index.php'>index.php</a> |
  <a href='/hello'>hello</a> |
  <a href='/redirect'>redirect</a> |

]

You are <b class='user'>
<?php
  print $_SESSION['Foo'];
?>
</b>

</div>
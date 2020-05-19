<!-- Bootstrap core JavaScript-->
<script src="assets/vendor/jquery/jquery.min.js"></script>
<script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

<!-- Core plugin JavaScript-->
<script src="assets/vendor/jquery-easing/jquery.easing.min.js"></script>

<!-- Custom scripts for all pages-->
<script src="js/sb-admin-2.min.js"></script>
<script>
    function switch_translate() {
        var current_label = document.getElementById('label1');
        if (current_label.innerHTML === 'Sunda') {
            document.getElementById('label1').innerHTML = 'Indonesia';
            document.getElementById('label2').innerHTML = 'Sunda';
        } else {
            document.getElementById('label1').innerHTML = 'Sunda';
            document.getElementById('label2').innerHTML = 'Indonesia';
        }
    }
</script>

</body>

</html>
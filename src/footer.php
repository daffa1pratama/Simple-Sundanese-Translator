<!-- Bootstrap core JavaScript-->
<script src="assets/vendor/jquery/jquery.min.js"></script>
<script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

<!-- Core plugin JavaScript-->
<script src="assets/vendor/jquery-easing/jquery.easing.min.js"></script>

<!-- Custom scripts for all pages-->
<script src="js/sb-admin-2.min.js"></script>
<script>
    $('#switchbtn').on('click', function() {
        $(document).ready(function() {
            var label1 = $('#label1');
            var label2 = $('#label2');
            if (label1.text() === 'Indonesia') {
                label1.html('Sunda');
                label2.html('Indonesia');
            } else {
                label1.html('Indonesia');
                label2.html('Sunda');
            }
            document.cookie = escape('label1') + "=" + escape(label1.text());
        });
    });
</script>

</body>

</html>
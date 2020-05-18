<?php require_once 'header.php'; ?>
<div class="container col-lg">

    <!-- Outer Row -->
    <div class="row justify-content-center">

        <div class="col-lg my-auto">

            <div class="card o-hidden border-0 shadow-lg my-5">
                <div class="card-body p-0">
                    <!-- Nested Row within Card Body -->
                    <div class="row">
                        <div class="col-lg">
                            <div class="p-5">
                                <div class="text-center">
                                    <h1 class="h1 text-gray-900 mb-4">Sundanese Translator</h1>
                                </div>
                                <form class="user" action="http://localhost/Simple-Sundanese-Translator/src/test.php">
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label for="exampleFormControlTextarea1">Example textarea</label>
                                                <textarea class="form-control" id="text1" name="text1" rows="10"></textarea>
                                            </div>
                                            <button type="submit" class="btn btn-primary btn-user btn-block" name="btn1">
                                                Login
                                            </button>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label for="exampleFormControlTextarea1">Example textarea</label>
                                                <textarea class="form-control" id="text1" name="text1" rows="10"></textarea>
                                            </div>
                                            <button type="submit" class="btn btn-primary btn-user btn-block">
                                                Login
                                            </button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>



<?php require_once 'footer.php'; ?>
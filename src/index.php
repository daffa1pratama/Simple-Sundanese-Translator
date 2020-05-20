<?php require_once 'header.php'; ?>

<div class="container col-lg">
    <div class="row justify-content-center">
        <div class="col-lg my-auto">
            <div class="card o-hidden border-0 shadow-lg my-5">
                <div class="card-body p-0">
                    <div class="row">
                        <div class="col-lg">
                            <div class="p-5">
                                <div class="text-center">
                                    <h1 class="h1 text-gray-900">Sundanese Translator</h1>
                                </div>
                                <div class="row justify-content-center">
                                    <div class="col-lg-5">
                                        <form class="user" action="" method="POST">
                                            <div class="form-group">
                                                <p class="text-center" id="label1">Indonesia</p>
                                                <textarea style="resize:none" class="form-control" id="text1" name="text1" rows="10" autofocus><?php if (isset($_POST['btn1'])) echo $_POST['text1']; ?></textarea>
                                            </div>
                                            <button type="submit" class="btn btn-primary btn-user btn-block" name="btn1" id="btn1">
                                                Translate
                                            </button>
                                        </div>
                                        <div class="col-lg-1 text-center">
                                            <button class="btn" type="button" name="switchbtn" id="switchbtn">
                                                <i class="fas fa-exchange-alt"></i>
                                            </button>
                                            <div class="form-group">
                                                <label for="algorithm">Algorithm</label>
                                                <select class="form-control" id="algorithm" name="algorithm">
                                                    <option value="KMP">KMP</option>
                                                    <option value="BM">BM</option>
                                                    <option value="Regex">Regex</option>
                                                </select>
                                            </div>
                                            <div class="form-group">
                                                <label for="find">Find method</label>
                                                <select class="form-control" id="find" name="find">
                                                    <option value="All">All</option>
                                                    <option value="First">First</option>
                                                </select>
                                            </div>
                                        </form>
                                    </div>
                                    <div class="col-lg-5">
                                        <div class="form-group">
                                            <p class="text-center" id="label2">Sunda</p>
                                            <textarea style="resize:none" class="form-control" id="text2" name="text2" rows="10" disabled><?php
                                                if (isset($_POST['btn1'])) {
                                                    if (!empty($_POST['text1'])) {
                                                        $find = $_POST['find'];
                                                        $algorithm =  $_POST['algorithm'];
                                                        $translate = $_COOKIE['label1'];
                                                        $command = escapeshellcmd("python main.py " . $translate . " " . $algorithm . " " . $find . " " . $_POST['text1']);
                                                        $output = shell_exec($command);
                                                        echo $output; 
                                                    }
                                                }?>
                                            </textarea>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<?php require_once 'footer.php'; ?>
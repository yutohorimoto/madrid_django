    //問題と解答
    qa = new Array();
    qa[0] = ["レアルマドリードのCL優勝回数は？","１０回","１１回","１２回","１３回",4];
    qa[1] = ["レアルマドリードで１０番をつけたことがないのは？","ルイス・フィーゴ","ジダン","スナイデル","メスト・エジル",2];
    qa[2] = ["２０１４年のCL決勝アトレティコマドリード戦で後半ロスタイムに同点ゴールを決めたのは？","クリスティアーノ・ロナウド","セルヒオ・ラモス","ギャレス・ベイル","ディ・マリア",2];
    qa[3] = ["２０１３－２０１５年の監督は？","モウリーニョ","ジダン","アンチェロッティ","ベニテス",3];
    qa[4] = ["クリスティアーノ・ロナウドのレアルマドリードでの得点数は？","３０１得点","３５１得点","４０１得点","４５１得点",4];
    qa[5] = ["レアルマドリードのホームスタジアムの名前は？","サンチャゴ・ベルナベウ","カンプ・ノウ","オールド・トラフォード","ワンダ・メトロポリターノ",1];
    qa[6] = ["２０１８年のCL決勝リヴァプール戦で２ゴールを記録したのは？","クリスティアーノ・ロナウド","カリム・ベンゼマ","ギャレス・ベイル","ルカ・モドリッチ",3];
    qa[7] = ["レアルマドリードでのラリーガ最多出場記録保持者は？","イケル・カシージャス","ラウール・ゴンザレス","セルヒオ・ラモス","アルフレッド・ディ・ステファノ",2];
    qa[8] = ["グティの後にレアルマドリードの背番号14をつけた選手は？","シャビ・アロンソ","ハビエル・エルナンデス","カゼミーロ","ケディラ",1];
    qa[9] = ["クラシコ歴代最多出場選手は？","マヌエル・サンチェス","シャビ・エルナンデス","イケル・カシージャス","セルヒオ・ラモス",4];

        //初期設定
    count = 0; //問題番号
    q_sel = 4; //選択肢の数
    point = 0;

    //最初の問題
    quiz();

//問題表示
function quiz() {
	var s, n;
	//問題
	document.getElementById("text_q").innerHTML = (count + 1) + "問目：" + qa[count][0];
	//選択肢
	s = "";
	for (n=1;n<=q_sel;n++) {
		s += "【<a href='javascript:anser(" + n + ")'>" + n + "：" + qa[count][n] + "</a>】";
	}
	document.getElementById("text_s").innerHTML = s;
}

//解答表示
function anser(num) {
	var s;
	s = (count + 1) + "問目：";
	//答え合わせ
	if (num == qa[count][q_sel + 1]) {
		//正解
        s += "○" + qa[count][num];
        point += 10;
	} else {
		s += "×" + qa[count][num];
	}
    document.getElementById("text_a").innerHTML = s;
    
    //次の問題を表示
	count++;
	if (count < qa.length) {
        quiz();
        document.getElementById("text_p").innerHTML = point;
	} else {
		//終了
		document.getElementById("text_q").innerHTML = "";
        document.getElementById("text_s").innerHTML = "";
        //document.getElementById("text_p").innerHTML = point;
        if(point>=70){
            document.getElementById("text_p").innerHTML =point+ "  よくできました。"
        }else{
            document.getElementById("text_p").innerHTML =point+ "  まだまだです。"
        }
	}
}
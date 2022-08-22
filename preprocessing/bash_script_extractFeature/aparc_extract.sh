printf "subjectID,caudalanteriorcingulate_SurfArea,caudalanteriorcingulate_GrayVol,caudalanteriorcingulate_ThickAvg,caudalanteriorcingulate_ThickStd,caudalanteriorcingulate_MeanCurv,">>aparcData.csv

printf "caudalmiddlefrontal_SurfArea,caudalmiddlefrontal_GrayVol,caudalmiddlefrontal_ThickAvg,caudalmiddlefrontal_ThickStd,caudalmiddlefrontal_MeanCurv,">>aparcData.csv

printf "cuneus_SurfArea,cuneus_GrayVol,cuneus_ThickAvg,cuneus_ThickStd,cuneus_MeanCurv,">>aparcData.csv

printf "entorhinal_SurfArea,entorhinal_GrayVol,entorhinal_ThickAvg,entorhinal_ThickStd,entorhinal_MeanCurv,">>aparcData.csv

printf "fusiform_SurfArea,fusiform_GrayVol,fusiform_ThickAvg,fusiform_ThickStd,fusiform_MeanCurv,">>aparcData.csv

printf "inferiorparietal_SurfArea,inferiorparietal_GrayVol,inferiorparietal_ThickAvg,inferiorparietal_ThickStd,inferiorparietal_MeanCurv,">>aparcData.csv

printf "inferiortemporal_SurfArea,inferiortemporal_GrayVol,inferiortemporal_ThickAvg,inferiortemporal_ThickStd,inferiortemporal_MeanCurv,">>aparcData.csv

printf "isthmuscingulate_SurfArea,isthmuscingulate_GrayVol,isthmuscingulate_ThickAvg,isthmuscingulate_ThickStd,isthmuscingulate_MeanCurv,">>aparcData.csv

printf "lateraloccipital_SurfArea,lateraloccipital_GrayVol,lateraloccipital_ThickAvg,lateraloccipital_ThickStd,lateraloccipital_MeanCurv,">>aparcData.csv

printf "lateralorbitofrontal_SurfArea,lateralorbitofrontal_GrayVol,lateralorbitofrontal_ThickAvg,lateralorbitofrontal_ThickStd,lateralorbitofrontal_MeanCurv,">>aparcData.csv

printf "lingual_SurfArea,lingual_GrayVol,lingual_ThickAvg,lingual_ThickStd,lingual_MeanCurv,">>aparcData.csv

printf "medialorbitofrontal_SurfArea,medialorbitofrontal_GrayVol,medialorbitofrontal_ThickAvg,medialorbitofrontal_ThickStd,medialorbitofrontal_MeanCurv,">>aparcData.csv

printf "middletemporal_SurfArea,middletemporal_GrayVol,middletemporal_ThickAvg,middletemporal_ThickStd,middletemporal_MeanCurv,">>aparcData.csv

printf "parahippocampal_SurfArea,parahippocampal_GrayVol,parahippocampal_ThickAvg,parahippocampal_ThickStd,parahippocampal_MeanCurv,">>aparcData.csv

printf "paracentral_SurfArea,paracentral_GrayVol,paracentral_ThickAvg,paracentral_ThickStd,paracentral_MeanCurv,">>aparcData.csv

printf "parsopercularis_SurfArea,parsopercularis_GrayVol,parsopercularis_ThickAvg,parsopercularis_ThickStd,parsopercularis_MeanCurv,">>aparcData.csv

printf "parsorbitalis_SurfArea,parsorbitalis_GrayVol,parsorbitalis_ThickAvg,parsorbitalis_ThickStd,parsorbitalis_MeanCurv,">>aparcData.csv

printf "parstriangularis_SurfArea,parstriangularis_GrayVol,parstriangularis_ThickAvg,parstriangularis_ThickStd,parstriangularis_MeanCurv,">>aparcData.csv

printf "pericalcarine_SurfArea,pericalcarine_GrayVol,pericalcarine_ThickAvg,pericalcarine_ThickStd,pericalcarine_MeanCurv,">>aparcData.csv

printf "postcentral_SurfArea,postcentral_GrayVol,postcentral_ThickAvg,postcentral_ThickStd,postcentral_MeanCurv,">>aparcData.csv

printf "posteriorcingulate_SurfArea,posteriorcingulate_GrayVol,posteriorcingulate_ThickAvg,posteriorcingulate_ThickStd,posteriorcingulate_MeanCurv,">>aparcData.csv

printf "precentral_SurfArea,precentral_GrayVol,precentral_ThickAvg,precentral_ThickStd,precentral_MeanCurv,">>aparcData.csv

printf "precuneus_SurfArea,precuneus_GrayVol,precuneus_ThickAvg,precuneus_ThickStd,precuneus_MeanCurv,">>aparcData.csv

printf "rostralanteriorcingulate_SurfArea,rostralanteriorcingulate_GrayVol,rostralanteriorcingulate_ThickAvg,rostralanteriorcingulate_ThickStd,rostralanteriorcingulate_MeanCurv,">>aparcData.csv

printf "rostralmiddlefrontal_SurfArea,rostralmiddlefrontal_GrayVol,rostralmiddlefrontal_ThickAvg,rostralmiddlefrontal_ThickStd,rostralmiddlefrontal_MeanCurv,">>aparcData.csv

printf "superiorfrontal_SurfArea,superiorfrontal_GrayVol,superiorfrontal_ThickAvg,superiorfrontal_ThickStd,superiorfrontal_MeanCurv,">>aparcData.csv

printf "superiorparietal_SurfArea,superiorparietal_GrayVol,superiorparietal_ThickAvg,superiorparietal_ThickStd,superiorparietal_MeanCurv,">>aparcData.csv

printf "superiortemporal_SurfArea,superiortemporal_GrayVol,superiortemporal_ThickAvg,superiortemporal_ThickStd,superiortemporal_MeanCurv,">>aparcData.csv

printf "supramarginal_SurfArea,supramarginal_GrayVol,supramarginal_ThickAvg,supramarginal_ThickStd,supramarginal_MeanCurv,">>aparcData.csv

printf "frontalpole_SurfArea,frontalpole_GrayVol,frontalpole_ThickAvg,frontalpole_ThickStd,frontalpole_MeanCurv,">>aparcData.csv

printf "temporalpole _SurfArea,temporalpole _GrayVol,temporalpole _ThickAvg,temporalpole _ThickStd,temporalpole _MeanCurv,">>aparcData.csv

printf "transversetemporal_SurfArea,transversetemporal_GrayVol,transversetemporal_ThickAvg,transversetemporal_ThickStd,transversetemporal_MeanCurv,">>aparcData.csv

printf "insula_SurfArea,insula_GrayVol,insula_ThickAvg,insula_ThickStd,insula_MeanCurv,">>aparcData.csv


echo "">> aparcData.csv




for subj_id in $(ls /home/jijinling/ADNI/CN_bash_test/bash_test/ADNI1_Complete_1Yr_1.5T_CN/processed); do

printf "%s,"  "${subj_id%%//}" >> aparcData.csv

for x in caudalanteriorcingulate caudalmiddlefrontal cuneus entorhinal fusiform inferiorparietal inferiortemporal isthmuscingulate lateraloccipital lateralorbitofrontal lingual medialorbitofrontal middletemporal parahippocampal paracentral parsopercularis parsorbitalis parstriangularis pericalcarine postcentral posteriorcingulate precentral precuneus rostralanteriorcingulate rostralmiddlefrontal superiorfrontal superiorparietal superiortemporal supramarginal frontalpole temporalpole transversetemporal insula; do

printf "%g,%g,%g,%g,%g," `grep ${x} ./processed/${subj_id}/bert/stats/lh.aparc.stats | awk '{print $3,$4,$5,$6,$7}'` >> aparcData.csv

done

   echo "">> aparcData.csv

done

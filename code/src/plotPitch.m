clear all;

formatSpec = '%f %f';
prompt = 'Enter the absolute pathName of the dir: ';
dirName = input(prompt,'s');
files = dir(dirName);

plotInd = 1;
for file = files'
    fileID = fopen(file.name, 'r');
    sizeA = [2 Inf];
    A = fscanf(fileID, formatSpec, sizeA);
    A = A';

    subplot(2, 5, plotInd);
    plot(A(2:end, 1), A(2:end, 2));
    axis([0, 31, 0, 1000]);
    title(file.name);
    
    plotInd = plotInd + 1;
end
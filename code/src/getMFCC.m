clear all;

prompt = 'Enter the absolute pathName of the dir: ';
dirName = input(prompt, 's');
files = dir(dirName);

fileID = fopen('mfccFeatures.txt','a+');
for file = files'
  wavFile = wavread(file.name);
  ceps = mfcc(wavFile, 44100);
  ceps = ceps';
  fprintf(fileID, '%f,', mean(ceps));
  fprintf(fileID, '%f,', var(ceps));
  fprintf(fileID, '\n');
end
fclose(fileID);

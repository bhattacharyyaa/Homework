MA <- matrix(c(7,2,9,4,12,13),nrow=2,ncol=3)
MB <- matrix(c(1,2,3,7,8,9,12,13,14,19,20,21), nrow=3,ncol=4)
MC <- A %*% B

print(MC)

Data_frame<- data.frame(ID=c(1,2,3,4,5),Name=c("Peter","Amy","Ryan","Gary","Michelle"), Salary=c(623.3,515.2,611,729,843.25))
print(Data_frame)

new_col_DF<-cbind(Data_frame, Department=c("Tech","Secretarial","HR","IT","Managment"))
print(new_col_DF)

new_col_DF[c(1,3,5),(2:3)]



barplot(Data_frame$Salary,col="pink", names.arg= new_col_DF$Name)

max=max(new_col_DF$Salary)
min=min(new_col_DF$Salary)
med=median(new_col_DF$Salary)
print(med)

pi=rbind(max,min,med)
print(pi)

pie(pi, label=new_col_DF$Name, main="Salary Data")







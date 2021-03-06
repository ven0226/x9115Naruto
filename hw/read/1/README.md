# Summary

## (i) Reference : C. Sun, D. Lo, S.-C. Khoo, and J. Jiang. Towards more accurate retrieval of duplicate bug reports. In ASE'11, pages 253-262. IEEE CS, 2011

## (ii) Keywords

* (ii1) **Bugs** : A software bug is an error, flaw, failure, or fault in a computer program or system that causes it to produce an incorrect or unexpected result, or to behave in unintended ways.

* (ii2) **Bug tracking system** : A bug tracking system is a software application that keeps track of reported software bugs in software development projects.

* (ii3) **Gradient Descent**: Gradient descent is a first-order optimization algorithm. To find a local minimum of a function using gradient descent, one takes steps proportional to the negative of the gradient (or of the approximate gradient) of the function at the current point.

* (ii4) **Similarity Measure**: A similarity measure is a real-valued function that quantifies the similarity between two objects. Usually similarity measures are in some sense the inverse of distance metrics: they take on large values for similar objects and either zero or a negative value for very dissimilar objects.

## (iii) Artifacts

* (iii1) **Motivational Statements**:

Bug reporting however is an uncoordinated distributed process. End users and testers might report the same defects many times in the bug reporting system. This causes an issue as different developers should not be assigned the same defect. Figuring out which bug reports are duplicate of others is typically done manually by a person called the triager. The triager would detect if a bug report is a duplicate; if it is, the triager would mark this report as a duplicate report and the first report as the master report. This process however is not scalable for systems with large user base as the process could take much time. One bug report might only provide a partial view of the defect, while multiple bug reports can complement one another. Thus, this study focuses on providing a technique that could help in linking bug reports that are duplicate of one another.

* (iii2) **Related Work**:

  * Natural language text of bug reports and perform standard tokenization, stemming, and stop word removal: . Runeson, M. Alexandersson, and O. Nyholm, “Detection of Duplicate Defect Reports Using Natural Language Processing,” in proceedings of the International Conference on Software Engineering, 2007.
  * Feature vector construction approach: X. Wang, L. Zhang, T. Xie, J. Anvik, and J. Sun, “An Approach to Detecting Duplicate Bug Reports using Natural Language and Execu- tion Information,” in proceedings of the International Conference on Software Engineering, 2008.
  * Classification technique to detect bug reports that are duplicated : N. Jalbert and W. Weimer, “Automated Duplicate Detection for Bug Tracking Systems,” in proceedings of the International Conference on Dependable Systems and Networks, 2008
  * Discriminative approach to detect bug reports using SVM: C. Sun, D. Lo, X. Wang, J. Jiang, and S.-C. Khoo, “A discriminative model approach for accurate duplicate bug report retrieval,” in ICSE, 2010, pp. 45–56.
  * An approach that consider not word tokens but n-grams as features in a feature vector : A. Sureka and P. Jalote, “Detecting duplicate bug report using character n-gram-based features,” in Proceedings of the 2010 Asia Pacific Software Engineering Conference, 2010, pp. 366–374.



* (iii3) **Commentary**:

Paper uses the bug repositories of three large open source projects: OpenOffice, Mozilla and Eclipse. OpenOffice is an open source counterpart of Microsoft Office. Mozilla is a community hosting multiple open source projects such as Firefox Thunderbird. Eclipse is an extensible multi-language software development environment written in Java. There are four report datasets from them by choosing reports submitted within a period of time T. In particular, two datasets from Eclipse: one is for reports submitted in 2008, whereas the other is for reports submitted from the beginning of Eclipse project to 2007. Since our retrieval function involves the order of versions, they manually recovered the chronological order of all the versions for OpenOffice by searching the release date of each version on the internet.

* (iii4) **Future Work**:

They plan to build indexing structure of bug report repository to speed up the retrieval process. They also plan to integrate the technique into Bugzilla tracking system.

## (iv) Improvements:

* (iv1) The key assumption in REP is based on high textual similarity between duplicate bug reports. It is possible that the bug reports can be filed by multiple reporters who could describe about the same technical issue in different phenomena via different terms.

* (iv2) The BM25F model was picked directly. No comparison study with other textual similarity algorithms was carried out.

* (iv3) The experimental setup and dataset could have been uploaded to a public repository for reference.


;; M-x: wl to immediately read WorkLog filel
(defun wl ()
  "opens a worklog file"
  (interactive)
  (find-file "~/orgnotes/WL.org")
  )

;; set default keys for org-mode todo
;; for each mode change record a time stamp
(setq org-todo-keywords
      '((sequence "TODO" "PROGRESS(/!)" "DONE(/!)"))
      )

;; set a timestamp when some items are done
(setq org-log-done 'time)  ;; use 'note for note taking

;; set tags for common task context
(setq org-tag-alist '(
                      (:startgroup . nil)
                      ("#work" . ?w)
                      ("#personal" . ?p)
                      (:startgroup . nil)
                      ("reading" . ?r)
                      ("writing" . ?r)
                      ("family" . ?f)
                      ("enjoy" . ?e)
                      ))


;; onLoad org mode hook
;; find if there is a corresponding file in the remote
;; if there is then rsync it and reload
;; if there is not then keep going
(defun sync-from-cloud-if-possible()
  (interactive)
  (when (org-file-not-readme)
    (shell-command-to-string (format "python ~/orgsync/rsyncpull.py %s" buffer-file-name))
    (message "Done pulling!")
    )
  )

(add-hook 'after-change-major-mode-hook #'sync-from-cloud-if-possible)



;; Add hooks afterSave
;; while the mode is org-mode
;; call python syncer. 
(defun sync-to-cloud ()
  "Sync org file to github repo"
  (interactive)
  (when (org-file-not-readme)
    (shell-command-to-string (format "python ~/orgsync/rsyncpush.py %s" buffer-file-name))
    (message "Done rsyncing")
    ))

(add-hook 'after-save-hook #'sync-to-cloud)


;; minor functions required by hooks
(defun file-is-readme ()
  (eq (file-name-base (format "%s" buffer-file-name)) "README")
  )

(defun org-file-not-readme ()
  (and (not (file-is-readme)) (eq major-mode 'org-mode))
  )

;;(package-initialize)
;;(elpy-enable)


;; Save desktop session before exiting and on auto save
;; reload them when emacs is started again
(require 'desktop)
(desktop-save-mode 1)
(defun my-desktop-save ()
  (interactive)
  ;; Don't call desktop-save-in-desktop-dir, as it prints a message.
  (if (eq (desktop-owner) (emacs-pid))
      (desktop-save desktop-dirname)))
 (add-hook 'auto-save-hook 'my-desktop-save)



;; Function to insert todays entry if one doesnot exist already
(defun org-note-add-todays-entry ()
  "Insert todays entry if one doesnot exist already"
  (interactive)
  (insert "\n")
  (insert (format "* %s" (org-note-todays-stamp)))
  (insert "

** Q1 Task(Urgent & Important)             
*** TODO 

** Q2 Task(Urgent & Not Important)         
*** 

** Q3 Task(Not-urgent & Important)         
*** 

** Q4 Task(Neither Urgent nor Imporntant)  
*** 

** Todays Journal
  ")
  )


(defun org-note-todays-stamp ()
  "generate formatted date from todays date"
  (format-time-string "%a %m-%d-%Y")
  )


;; carry over unfinished tasks to new entry respecting priorities
;; When a task is carried over, it will be linked to the previous
;; entry via a target. 
;; This preserves the origination of the task
;; and allow one to visualize how long it took to complete it.
;;
;; TODO: check if this can be acheived by org-mode agenda view.
(defun org-note-carry-over-incomplete-tasks ()
  ()
 )


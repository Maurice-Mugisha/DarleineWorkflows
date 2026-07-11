<?php


if(isset($_GET['specific_step'])):


	$step_id = isset($_GET['step_id']) ? $fieldValidator->validate_field($_GET['step_id']) : "";

	$workflowstepmap_array = array();
	$step_array = array();
	$workflow_array = array();

	$query = $queryExecutor->execute($selectionObj->select_step($step_id));

	while($row = mysqli_fetch_array($query)):

		$step_id = $row['step_id'];
		$step_array[$step_id] = array();
		$step_array[$step_id]['step_id'] = $step_id;

		$key = $step_id;


		$secondary_query = $queryExecutor->execute($selectionObj->select_workflowstepmap_by_step($step_id));

		while($sec_row = mysqli_fetch_array($secondary_query)):

			$workflow_id = $sec_row['workflow_id'];
			$workflow_array[$workflow_id] = array();
			$workflow_array[$workflow_id]['workflow_id'] = $workflow_id;

			$sec_key = $workflow_id;

		endwhile;



	endwhile;


?>

<table cellspacing = "1" cellpadding = "0" align = "center" width = "100%" id = "workflowstepmap">
 <tr>
 <td colspan = "3">&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td colspan = "2"><a href="target_print.php?workflowstepmap&&step_id=<?= $step_id ?>" target="_blank" style="color:#00FF00;">Print PDF</a></td></tr>
 <tr class = "top_row">
 <td>&nbsp;&nbsp;#&nbsp;&nbsp;</td>
 <td>&nbsp;Workflow id&nbsp;</td>
 <td>&nbsp;Name&nbsp;</td>
 <td>&nbsp;Workspace id&nbsp;</td>
 <td>&nbsp;&nbsp;Actions&nbsp;&nbsp;</td></tr>
 
<?php $i = 0; ?>


<?php  foreach($workflow_array as $workflow_key => $workflow_value): ?>
<?php $css_class = ($i+1)%2 == 0 ? "even_row" : "odd_row"; ?>


<tr>
	<td><?= ($i+1) ?></td>
	<td><?= $workflow_value['workflow_id'] ?></td>
	<td><?= $workflow_value['name'] ?></td>
	<td><?= $workflow_value['workspace_id'] ?></td>
	<td>

		<?php $id_string = $workflow_id; ?>

		<div id="update_workflow_<?= $id_string ?>" style="display:none" class="updates">
		<table border="0" align="center" class="overlay_contained_table">
		<tr>
			<td align="right">
			<div class="closebtn" id="close_circle" onclick="closeUpdateOverlay('update_workflow_<?= $id_string ?>');">&nbsp;&times;&nbsp;</div>
			</td>
		</tr>
		<tr><td><br /></td></tr>
		<tr>
			<td align="center">
			<fieldset style="width: 80%">
			<legend>workflow Information</legend>
			<?php update_workflow($queryExecutor, $selectionObj, $updateObj, $fieldValidator, $workflow_value['workflow_id']); ?>
			</fieldset>
			</td>
		</tr>
		<tr>
			<td><br /></td>
		</tr>
		</table>
		</div>


<?php

	$workflowstepmap_count = count_workflowstepmap($queryExecutor, $selectionObj);
	$mapping_link = "workflowstepmap.php?workflow&&workflow_id=".$workflow_value['workflow_id']."";
	$title = "workflowstepmap corresponding entries.";
	$label = "Wor.";
	get_mapping_mark_up($workflowstepmap_count, $mapping_link, $title, $label);



?>


	<label id="update_link_<?= $id_string ?>" onclick="showUpdate('update_<?= $id_string ?>');" style="cursor:pointer">
	<img src="images/icons/edit.png" width="15px" height="15px" title="edit entry" style="cursor:pointer" />
	</label> 
 &nbsp; 
	<?php 
		$link = "workflow.php?delete_Workflow&&workflow_id=".$workflow_value['workflow_id']."";
		$message = "";
	?>

	<?php showConfirmDeleteAction($id_string, $link, $message); ?>
	<label style="cursor:pointer" onclick="showDelete('delete_<?= $id_string ?>')">
	<img src="images/icons/delete.png" width="15px" height="15px" title="delete entry" />
	</label>
	</td>
<tr>
	<?php $i = ($i + 1); ?>
<?php endforeach; ?>
 <tr>
 <td colspan = "5"></td></tr></table>

<?php endif; ?>

